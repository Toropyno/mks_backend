from sqlalchemy.exc import DBAPIError

from mks_backend.repositories import DBSession


class DBBasicError(DBAPIError):
    codes = {
        'other_error': 'Ошибка с БД!',

        'construction_project_code_key_duplicate': 'Проект с указанным ключом уже существует!',
        'commission_code_key_duplicate': 'Комиссия с указанным ключом уже существует!',
        'commission_fullname_key_duplicate': 'Комиссия с указанным именем уже существует!',

        'construction_subcategories_fullname_key_duplicate': 'Подкатегория с указанным наименованием уже существует!',
        'construction_categories_fullname_key_duplicate': 'Категория с указанным наименованием уже существует!',

        'subcategories_list_unique_duplicate': 'Перечень Подкатегорий с указанными Категорией и Подкатегорией уже '
                                               'существует!',
        'object_categories_list_unique_duplicate': 'Перечень Категорий Объектов с указанными Зоной Военного Городка и '
                                                   'Категорией Объектов уже существует!',

        'construction_objects_object_code_key_duplicate': 'Объект Строительства с таким кодом уже существует!',
        'construction_stages_code_key_duplicate': 'Этап Строительства с таким кратким наименованием уже существует!',
        'construction_stages_fullname_key_duplicate': 'Этап Строительства с таким полным наименованием уже существует!',
        'object_categories_list_zones_id_key_duplicate': 'Перечень Категорий Объектов с указанной Зоной Военного '
                                                         'Городка уже существует!',
        'object_categories_list_object_categories_id_key_duplicate': 'Перечень Категорий Объектов с указанной '
                                                                     'Категорией Объекта Строительства уже существует!',
        'object_categories_fullname_key_duplicate': 'Категория Объекта Строительства с таким наименованием уже '
                                                    'существует!',

        'zones_fullname_key_duplicate': 'Зона Военного Городка с таким наименованием уже существует!',

        'other_duplicate': 'Дубликат записи!',

        'construction_construction_categories_id_fkey': 'Категории Проекта с указанным ключом не существует!',
        'construction_subcategories_list_id_fkey': 'Перечня Подкатегорий Проекта с указанным ключом не существует!',
        'construction_commission_id_fkey': 'Комиссии с указанным ключом не существует!',
        'construction_idMU_fkey': 'Воинского Формирования с указанным ключом не существует!',

        'construction_objects_construction_id_fkey': 'Указанного Проекта не существует!',
        'construction_objects_object_categories_list_id_fkey': 'Указанного Перечня Категорий Объектов не существует!',
        'construction_objects_zones_id_fkey': 'Указанной Зоны Военного Городка не существует!',
        'construction_objects_construction_stages_id_fkey': 'Указанного Этапа Строительства не существует!',
        'object_categories_list_zones_id_fkey': 'Указанной Зоны Военного Городка не существует!',
        'object_categories_list_object_categories_id_fkey': 'Указанной Категории Объекта Строительства не существует!',

        'other_fkey': 'Вторичный ключ не найден!',
    }

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
    def message(self, pg_error: str) -> None:
        code = self.get_error_code(pg_error)
        self._message = self.codes[code]

    @code.setter
    def code(self, pg_error: str) -> None:
        self._code = self.get_error_code(pg_error)

    def get_error_code(self, pg_error: str) -> str:

        if 'duplicate' in pg_error:
            '''
            ERROR:  duplicate key value violates unique constraint "construction_project_code_key"
            DETAIL:  Key (project_code)=(12345) already exists.
            '''

            start = pg_error.find('constraint') + 12
            end = pg_error.find('\"', start)
            code = pg_error[start:end] + '_duplicate'

            if code not in self.codes:
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

            if code not in self.codes:
                code = 'other_fkey'

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
