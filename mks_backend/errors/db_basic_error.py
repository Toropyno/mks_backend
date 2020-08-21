from sqlalchemy.exc import DBAPIError


class DBBasicError(DBAPIError):
    codes = {
        'other_error': 'Какая-то другая ошибка с БД!',

        'project_code_duplicate': 'Проект с таким кодом уже существует!',
        'other_duplicate': 'Какой-то другой дубликат!',

        'construction_categories_id_not_found': 'Такой категории проекта не существует!',
        'other_not_found': 'Какой-то другой foreign key не найден!',
    }

    def __init__(self, message):
        self.code = message
        self.message = message

    @property
    def message(self):
        return self._message

    @property
    def code(self):
        return self._code

    @message.setter
    def message(self, pg_error):
        code = self.get_error_code(pg_error)
        self._message = self.codes[code]

    @code.setter
    def code(self, pg_error):
        self._code = self.get_error_code(pg_error)

    @classmethod
    def get_error_code(cls, pg_error):
        if 'duplicate' in pg_error:
            '''
            ERROR:  duplicate key value violates unique constraint "construction_project_code_key"
            DETAIL:  Key (project_code)=(12345) already exists.
            '''
            code = pg_error[pg_error.index('(') + 1: pg_error.index(')')] + '_duplicate'

            if code not in cls.codes:
                code = 'other_duplicate'
        elif 'foreign key' in pg_error:
            '''
            ERROR:  insert or update on table "construction" violates foreign key constraint 
            "construction_construction_categories_id_fkey"
            DETAIL:  Key (construction_categories_id)=(6) is not present in table "construction_categories".
            '''
            code = code = pg_error[pg_error.index('(') + 1: pg_error.index(')')] + '_not_found'

            if code not in cls.codes:
                code = 'other_not_found'
        else:
            code = 'other_error'

        return code


def db_error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except DBAPIError as error:
            raise DBBasicError(error.orig.pgerror)
    return wrapper
