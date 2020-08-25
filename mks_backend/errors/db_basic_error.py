from sqlalchemy.exc import DBAPIError


class DBBasicError(DBAPIError):

    codes = {
        'other_error': 'Какая-то другая ошибка с БД!',
        'construction_project_code_key_duplicate': 'Проект с таким кодом уже существует!',
        'commission_code_key_duplicate': 'Комиссия с таким кодом уже существует!',
        'commission_fullname_key_duplicate': 'Комиссия с таким именем уже существует!',

        'other_duplicate': 'Какой-то другой дубликат!',

        'construction_objects_object_code_key_duplicate': 'Объект строительства с таким кодом уже существует!',
        'construction_stages_code_key_duplicate': 'Этап строительства с таким кратким наименованием уже существует!',
        'construction_stages_fullname_key_duplicate': 'Этап строительства с таким полным наименованием уже существует!',
        'object_categories_list_zones_id_key_duplicate': 'Перечень категорий объектов с указанной зоной военного '
                                                         'городка уже существует!',
        'object_categories_list_object_categories_id_key_duplicate': 'Перечень категорий объектов с указанной '
                                                                     'категорией объекта строительства уже существует!',
        'object_categories_fullname_key_duplicate': 'Категория объекта строительства с таким наименованием уже '
                                                    'существует!',
        'zones_fullname_key_duplicate': 'Зона военного городка с таким наименованием уже существует!',

        'construction_construction_categories_id_fkey': 'Такой категории проекта не существует!',
        'construction_subcategories_list_id_fkey': 'Такой подкатегории проекта не существует!',
        'construction_commission_id_fkey': 'Такой комиссии не существует!',
        'construction_idMU_fkey': 'Такого воинского формирования не существует!',

        'other_fkey': 'Какой-то другой foreign key не найден!',

        'construction_objects_construction_id_fkey': 'Указанного проекта не существует!',
        'construction_objects_object_categories_list_id_fkey': 'Указанного перечня категорий объектов не существует!',
        'construction_objects_zones_id_fkey': 'Указанной зоны военного городка не существует!',
        'construction_objects_construction_stages_id_fkey': 'Указанного этапа строительства не существует!',
        'object_categories_list_zones_id_fkey': 'Указанной зоны военного городка не существует!',
        'object_categories_list_object_categories_id_fkey': 'Указанной категорией объекта строительства не существует!'

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