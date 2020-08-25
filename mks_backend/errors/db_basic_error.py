from sqlalchemy.exc import DBAPIError


class DBBasicError(DBAPIError):
    codes = {
        'other_error': 'Ошибка с БД!',

        'construction_project_code_key_duplicate': 'Проект с указанным ключом уже существует!',
        'commission_code_key_duplicate': 'Комиссия с указанным ключом уже существует!',
        'commission_code_fullname_duplicate': 'Комиссия с указанным именем уже существует!',

        'construction_subcategories_fullname_key_duplicate': 'Подкатегория с указанным именем уже существует!',
        'construction_categories_fullname_key_duplicate': 'Категория с указанным именем уже существует!',

        'subcategories_list_construction_categories_id_key_duplicate': 'Перечень Подкатегорий с указанной Категорией '
                                                                       'уже существует!',
        'subcategories_list_construction_subcategories_id_key_duplicate': 'Перечень Подкатегорий с указанной '
                                                                          'Подкатегорией уже существует!',

        'other_duplicate': 'Дубликат записи!',

        'construction_construction_categories_id_fkey': 'Категории проекта с указанным ключом не существует!',
        'construction_subcategories_list_id_fkey': 'Подкатегории проекта с указанным ключом не существует!',
        'construction_commission_id_fkey': 'Комиссии с указанным ключом не существует!',
        'construction_idMU_fkey': 'Воинского Формирования с указанным ключом не существует!',
        'other_fkey': 'Вторичный ключ не найден!',
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
            code = pg_error[start:end] + '_duplicate'

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
