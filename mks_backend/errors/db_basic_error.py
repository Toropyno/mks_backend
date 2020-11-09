from sqlalchemy.exc import DBAPIError

from mks_backend.repositories import DBSession
from mks_backend.errors.db_error_codes import DB_ERROR_CODES


class DBBasicError(DBAPIError):
    codes = DB_ERROR_CODES

    def __init__(self, message: str):
        self.code = message
        self.message = message

    @property
    def message(self) -> str:
        return self._message

    @property
    def code(self) -> str:
        return self._code

    @message.setter
    def message(self, error_raw: str) -> None:
        code = self.get_error_code(error_raw)
        self._message = self.codes[code]

    @code.setter
    def code(self, error_raw: str) -> None:
        self._code = self.get_error_code(error_raw)

    def get_error_code(self, error_raw: str) -> str:

        if 'duplicate' in error_raw:
            '''
            ERROR:  duplicate key value violates unique constraint "construction_project_code_key"
            DETAIL:  Key (project_code)=(12345) already exists.
            '''

            start = error_raw.find('constraint') + 12
            end = error_raw.find('\"', start)
            code = error_raw[start:end] + '_duplicate'

            if code not in self.codes:
                code = 'other_duplicate'
        elif 'foreign key' in error_raw:
            '''
            ERROR:  insert or update on table "construction" violates foreign key constraint 
   
            "construction_construction_categories_id_fkey"
            DETAIL:  Key (construction_categories_id)=(6) is not present in table "construction_categories".
            '''

            start = error_raw.find('constraint') + 12
            end = error_raw.find('\"', start)
            code = error_raw[start:end]

            if code not in self.codes:
                code = 'other_fkey'
        elif 'nf' in error_raw:
            # entity not found in db
            code = error_raw
        elif 'limit' in error_raw:
            # logical limit for entity exceeded
            code = error_raw
        else:
            code = 'other_error'

        return code


def db_error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except DBAPIError as error:
            DBSession.rollback()
            raise DBBasicError(error.orig.pgerror)

    return wrapper
