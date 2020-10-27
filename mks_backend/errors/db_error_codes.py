DB_ERROR_CODES = {
        'other_error': 'Ошибка с БД!',

        'construction_project_code_key_duplicate': 'Проект с указанным ключом уже существует!',
        'commission_code_key_duplicate': 'Комиссия с указанным ключом уже существует!',
        'commission_fullname_key_duplicate': 'Комиссия с указанным именем уже существует!',

        'construction_subcategories_fullname_key_duplicate': 'Подкатегория с указанным наименованием уже существует!',
        'construction_categories_fullname_key_duplicate': 'Категория с указанным наименованием уже существует!',

        'location_types_fullname_key_duplicate': 'Тип местоположения с таким названием уже существует!',

        'construction_companies_unique_duplicate': 'Организация с таким кратким и полным названием уже существует!',

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
        'construction_types_fullname_key_duplicate': 'Такой тип проекта уже существует!',

        'leadership_positions_code_key_duplicate': 'Должность с таким кодом уже существует!',
        'leadership_positions_fullname_key_duplicate': 'Должность с таким наименованием уже существует!',

        'inspection_unique_duplicate': 'Поездка с такой датой и наименованием уже существует!',

        'fias_aoid_key_duplicate': 'FIAS с таким кодом уже существует!',

        'inspection_files_pkey_duplicate': 'Такой файл проверки уже существует!',


        'other_duplicate': 'Дубликат записи!',

        'protocol_meetings_type_id_fkey': ' Такого типа засдения не существует!',

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

        'work_trips_leadership_positions_id_fkey': 'Такой должности не существует!',
        'work_trips_protocol_id_fkey': 'Такого протокола не существует!',

        'inspection_objects_construction_id_fkey': 'Такого проверенного объекта строительства не существует!',
        'visited_objects_construction_id_fkey': 'Такого посещенного объекта строительства не существует!',

        'other_fkey': 'Вторичный ключ не найден!',
}
