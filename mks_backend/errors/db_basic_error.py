from .db_error_codes import DB_ERROR_CODES

from mks_backend._loggers import DBErrorLogger


class DBBasicError(Exception):
    codes = DB_ERROR_CODES

    def __init__(self, error_raw: str):
        self.error_raw = error_raw
        self.logger = DBErrorLogger()

    @property
    def code_and_message(self):
        code = self.get_error_code()
        if code not in self.codes:
            message = 'Ошибка c БД'
            self.logger.log(self.error_raw)
        else:
            message = self.codes[code]

        return {'code': code, 'message': message}

    def get_error_code(self) -> str:

        if 'duplicate' in self.error_raw:
            '''
            ERROR:  duplicate key value violates unique constraint "construction_project_code_key"
            DETAIL:  Key (project_code)=(12345) already exists.
            '''
            start = self.error_raw.find('constraint') + len('constraint "')
            end = self.error_raw.find('"', start)
            code = self.error_raw[start:end] + '_duplicate'

            if code not in self.codes:
                code = 'other_duplicate'
        elif 'foreign key' in self.error_raw:
            '''
            ERROR:  insert or update on table "construction" violates foreign key constraint    
            "construction_construction_categories_id_fkey"
            DETAIL:  Key (construction_categories_id)=(6) is not present in table "construction_categories".
            '''
            start = self.error_raw.find('constraint') + len('constraint "')
            end = self.error_raw.find('"', start)
            code = self.error_raw[start:end]

            if 'still referenced' in self.error_raw:
                code += '_sf'

            if code not in self.codes:
                code = 'other_fkey'
        elif 'nf' in self.error_raw:
            # entity not found in db
            code = self.error_raw
        elif 'limit' in self.error_raw:
            # logical limit for entity exceeded
            code = self.error_raw
        elif 'ad' in self.error_raw:
            # entity already deleted
            code = self.error_raw
        else:
            code = 'other_error'

        return code
