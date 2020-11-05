DB_ERROR_CODES = {
    'other_error': 'Ошибка с БД!',

    'commission_code_key_duplicate': 'Комиссия с указанным ключом уже существует!',
    'commission_fullname_key_duplicate': 'Комиссия с указанным именем уже существует!',
    'commission_pkey_duplicate': 'Комиссия с таким id уже существует!',
    'construction_project_code_key_duplicate': 'Проект с указанным ключом уже существует!',
    'construction_pkey_duplicate': 'Проект с таким id уже существует!',
    'construction_subcategories_fullname_key_duplicate': 'Подкатегория с указанным наименованием уже существует!',
    'construction_subcategories_pkey_duplicate': 'Подкатегория с таким id уже существует!',
    'construction_categories_fullname_key_duplicate': 'Категория с указанным наименованием уже существует!',
    'construction_categories_pkey_duplicate': 'Категория с таким id уже существует!',
    'location_types_fullname_key_duplicate': 'Тип Местоположения с таким названием уже существует!',
    'location_types_pkey_duplicate': 'Тип Местоположения с таким id уже существует!',
    'construction_companies_unique_duplicate': 'Организация с таким кратким и полным названием уже существует!',
    'construction_companies_pkey_duplicate': 'Организация с таким id уже существует!',
    'construction_objects_object_code_key_duplicate': 'Объект Строительства с таким кодом уже существует!',
    'construction_objects_pkey_duplicate': 'Объект Строительства с таким id уже существует!',
    'construction_stages_code_key_duplicate': 'Этап Строительства с таким кратким наименованием уже существует!',
    'construction_stages_fullname_key_duplicate': 'Этап Строительства с таким полным наименованием уже существует!',
    'construction_stages_pkey_duplicate': 'Этап Строительства с таким id уже существует!',
    'object_categories_pkey_duplicate': 'Категории Объектов Строительства с таким id уже существуют!',
    'object_categories_list_unique_duplicate': 'Перечень Категорий Объектов с указанной Зоной Военного Городка и '
                                               'Категорией Объекта Строительства уже существует!',
    'object_categories_fullname_key_duplicate': 'Категория Объекта Строительства с таким наименованием уже '
                                                'существует!',
    'zones_fullname_key_duplicate': 'Зона Военного Городка с таким наименованием уже существует!',
    'zones_pkey_duplicate': 'Зоны Военных Городков с таким id уже существуют!',
    'construction_types_fullname_key_duplicate': 'Такой Тип Проекта уже существует!',
    'construction_types_pkey_duplicate': 'Тип Проекта с таким id уже существует!',
    'leadership_positions_code_key_duplicate': 'Должность с таким кодом уже существует!',
    'leadership_positions_fullname_key_duplicate': 'Должность с таким наименованием уже существует!',
    'leadership_positions_pkey_duplicate': 'Должность с таким id уже существует!',
    'inspection_unique_duplicate': 'Поездка с такой датой и наименованием уже существует!',
    'inspection_files_pkey_duplicate': 'Файл Проверки с таким id уже существует!',
    'fias_aoid_key_duplicate': 'FIAS с таким кодом уже существует!',
    'fias_pkey_duplicate': 'FIAS с таким id уже существует!',
    'realty_types_fullname_key_duplicate': 'Тип Недвижимости с таким наименованием уже существует!',
    'realty_types_pkey_duplicate': 'Тип Недвижимости с таким id уже существует!',
    'progress_statuses_fullname_duplicate': 'Статусы Хода Работ с таким наименованием уже существуют!',
    'progress_statuses_pkey_duplicate': 'Статусы Хода Работ с таким id уже существует!',
    'OKSM_code_key_duplicate': 'ОКСМ с таким кодом уже существует!',
    'OKSM_shortname_key_duplicate': 'ОКСМ с таким коротким именем уже существует!',
    'OKSM_alpha2_key_duplicate': 'ОКСМ с таким буквенным кодом Альфа-2 уже существует!',
    'OKSM_alpha3_key_duplicate': 'ОКСМ с таким буквенным кодом Альфа-3 уже существует!',
    'OKSM_pkey_duplicate': 'ОКСМ с таким id уже существует!',

    'object_files_unique_duplicate': 'Объект Файлов с таким Файлом и Объектом Строительства уже существует!',
    'object_files_pkey_duplicate': 'Объект Файлов с таким id уже существует!',

    'subcategories_list_unique_duplicate': 'Перечень Подкатегорий с такими Категорией Проектов и Подкатегорией '
                                           'Проектов уже существует!',
    'subcategories_list_pkey_duplicate': 'Перечень Подкатегорий с таким id уже существует!',

    'other_duplicate': 'Дубликат записи!',

    'protocol_meetings_type_id_fkey': ' Такого Типа Заседания не существует!',
    'construction_construction_categories_id_fkey': 'Категории Проекта с указанным ключом не существует!',
    'construction_subcategories_list_id_fkey': 'Перечня Подкатегорий Проекта с указанным ключом не существует!',
    'construction_commission_id_fkey': 'Комиссии с указанным ключом не существует!',
    'construction_idMU_fkey': 'Воинского Формирования с указанным ключом не существует!',
    'construction_id_fias_fkey': 'ФИАС с указанным ключом не существует!',

    'construction_objects_construction_id_fkey': 'Указанного Проекта не существует!',
    'construction_objects_object_categories_list_id_fkey': 'Указанного Перечня Категорий Объектов не существует!',
    'construction_objects_zones_id_fkey': 'Указанной Зоны Военного Городка не существует!',
    'construction_objects_construction_stages_id_fkey': 'Указанного Этапа Строительства не существует!',

    'object_categories_list_zones_id_fkey': 'Указанной Зоны Военного Городка не существует!',
    'object_categories_list_object_categories_id_fkey': 'Указанной Категории Объекта Строительства не существует!',

    'subcategories_list_construction_categories_id_fkey': 'Указанной Категории Проектов не существует!',
    'subcategories_list_construction_subcategories_id_fkey': 'Указанной Подкатегории Проектов не существует!',

    'work_trips_leadership_positions_id_fkey': 'Такой Должности не существует!',
    'work_trips_protocol_id_fkey': 'Такого Протокола не существует!',

    'inspection_objects_construction_id_fkey': 'Такого Проверенного Объекта Строительства не существует!',
    'visited_objects_construction_id_fkey': 'Такого Посещенного Объекта Строительства не существует!',
    'construction_progress_progress_statuses_id_fkey': 'Такого Хода Строительства с таким Статусом Хода Работ не '
                                                       'существует!',

    'other_fkey': 'Вторичный ключ не найден!',
}
