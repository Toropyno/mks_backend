from sqlalchemy.exc import DBAPIError


class DBBasicError(DBAPIError):
    codes = {
        'other_error': 'Какая-то другая ошибка с БД!',

        'construction_project_code_key_duplicate': 'Проект с таким кодом уже существует!',
        'commission_code_key_duplicate': 'Комиссия с таким кодом уже существует!',
        'subcategories_list_key_duplicate': 'Комиссия с таким именем уже существует!',
        'subcategories_list_construction_categories_id_key_duplicate': "Введенный вторичный ключ(и) нарушает "
                                                                       "ограничение уникальности: введеный id уже "
                                                                       "имеется в перечне подкатегорий",
        'other_duplicate': 'Какой-то другой дубликат!',

        'construction_construction_categories_id_fkey': 'Такой категории проекта не существует!',
        'construction_subcategories_list_id_fkey': 'Такой подкатегории проекта не существует!',
        'construction_commission_id_fkey': 'Такой комиссии не существует!',
        'construction_idMU_fkey': 'Такой воинского формирования не существует!',
        'other_fkey': 'Какой-то другой foreign key не найден!',
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
            start = pg_error.find('constraint') + 12
            end = pg_error.find('\"', start)

            code = pg_error[start: end] + '_duplicate'

            if code not in cls.codes:
                code = 'other_duplicate'
        elif 'foreign key' in pg_error:
            '''
            ERROR:  insert or update on table "construction" violates foreign key constraint 
            "construction_construction_categories_id_fkey"
            DETAIL:  Key (construction_categories_id)=(6) is not present in table "construction_categories".
            '''
            start = pg_error.find('constraint') + 12
            end = pg_error.find('\"', start)
            code = pg_error[start:end]

            if code not in cls.codes:
                code = 'other_fkey'
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
