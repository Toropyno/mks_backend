from sqlalchemy.exc import DBAPIError

from mks_backend.models import DBSession
from mks_backend.errors.db_error_codes import DB_ERROR_CODES


class DBBasicError(Exception):
    codes = DB_ERROR_CODES

    def __init__(self, error_raw: str):
        self.error_raw = error_raw

    @property
    def message(self) -> None:
        return self.codes[self.code]

    @property
    def code(self) -> str:
        return self.get_error_code()

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


def db_error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except DBAPIError as error:
            DBSession.rollback()
            raise DBBasicError(error.orig.pgerror)

    return wrapper
