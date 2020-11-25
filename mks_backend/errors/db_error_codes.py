DB_ERROR_CODES = {
    'other_error': 'Ошибка с БД!',

    'commission_code_key_duplicate': 'Комиссия с указанным кодом уже существует!',
    'commission_fullname_key_duplicate': 'Комиссия с указанным наименованием уже существует!',
    'commission_pkey_duplicate': 'Комиссия с указанным ключом уже существует!',

    'construction_project_code_key_duplicate': 'Проект с указанным кодом уже существует!',
    'construction_pkey_duplicate': 'Проект с указанным ключом уже существует!',

    'construction_subcategories_fullname_key_duplicate': 'Подкатегория с указанным наименованием уже существует!',
    'construction_subcategories_pkey_duplicate': 'Подкатегория с указанным ключом уже существует!',

    'construction_categories_fullname_key_duplicate': 'Категория с указанным наименованием уже существует!',
    'construction_categories_pkey_duplicate': 'Категория с указанным ключом уже существует!',

    'location_types_fullname_key_duplicate': 'Тип Местоположения с указанным наименованием уже существует!',
    'location_types_pkey_duplicate': 'Тип Местоположения с указанным ключом уже существует!',

    'construction_companies_unique_duplicate': 'Организация с указанными кратким и полным названием уже существует!',
    'construction_companies_pkey_duplicate': 'Организация с указанным ключом уже существует!',

    'construction_objects_object_code_key_duplicate': 'Объект Строительства с указанным кодом уже существует!',
    'construction_objects_pkey_duplicate': 'Объект Строительства с указанным ключом уже существует!',

    'construction_stages_code_key_duplicate': 'Этап Строительства с указанным кодом уже существует!',
    'construction_stages_fullname_key_duplicate': 'Этап Строительства с указанным наименованием уже существует!',
    'construction_stages_pkey_duplicate': 'Этап Строительства с указанным ключом уже существует!',

    'object_categories_list_pkey_duplicate': 'Перечень Категорий Объектов с указанным ключом уже существует!',
    'object_categories_list_unique_duplicate': 'Перечень Категорий Объектов с указанными Зоной Военного Городка и '
                                               'Категорией Объекта Строительства уже существует!',

    'object_categories_pkey_duplicate': 'Категории Объектов Строительства с указанным ключом уже существуют!',
    'object_categories_fullname_key_duplicate': 'Категория Объекта Строительства с указанным наименованием уже '
                                                'существует!',

    'zones_fullname_key_duplicate': 'Зона Военного Городка с указанным наименованием уже существует!',
    'zones_pkey_duplicate': 'Зоны Военных Городков с указанным ключом уже существуют!',

    'construction_types_fullname_key_duplicate': 'Тип Проекта с указанным наименованием уже существует!',
    'construction_types_pkey_duplicate': 'Тип Проекта с указанным ключом уже существует!',

    'leadership_positions_code_key_duplicate': 'Должность с указанным кодом уже существует!',
    'leadership_positions_fullname_key_duplicate': 'Должность с указанным наименованием уже существует!',
    'leadership_positions_pkey_duplicate': 'Должность с указанным ключом уже существует!',

    'inspection_unique_duplicate': 'Поездка с указанной датой и именем уже существует!',

    'inspection_files_pkey_duplicate': 'Файл Проверки с указанным ключом уже существует!',

    'inspection_objects_pk_duplicate': 'Перечень Проверенных Объектов с указанным Проектом и Проверкой Объектов '
                                       'Строительства уже существует!',

    'fias_aoid_key_duplicate': 'FIAS с указанным AOID уже существует!',
    'fias_pkey_duplicate': 'FIAS с указанным ключом уже существует!',

    'realty_types_fullname_key_duplicate': 'Тип Недвижимости с указанным наименованием уже существует!',
    'realty_types_pkey_duplicate': 'Тип Недвижимости с указанным ключом уже существует!',

    'progress_statuses_fullname_key_duplicate': 'Статусы Хода Работ с указанным наименованием уже существуют!',
    'progress_statuses_pkey_duplicate': 'Статусы Хода Работ с указанным ключом уже существует!',

    'OKSM_code_key_duplicate': 'ОКСМ с указанным кодом уже существует!',
    'OKSM_shortname_key_duplicate': 'ОКСМ с указанным коротким именем уже существует!',
    'OKSM_alpha2_key_duplicate': 'ОКСМ с указанным буквенным кодом Альфа-2 уже существует!',
    'OKSM_alpha3_key_duplicate': 'ОКСМ с указанным буквенным кодом Альфа-3 уже существует!',
    'OKSM_pkey_duplicate': 'ОКСМ с указанным ключом уже существует!',

    'object_files_unique_duplicate': 'Объект Файлов с указанным Файлом и Объектом Строительства уже существует!',
    'object_files_pkey_duplicate': 'Объект Файлов с указанным ключом уже существует!',

    'subcategories_list_unique_duplicate': 'Перечень Подкатегорий с указанными Категорией Проектов и Подкатегорией '
                                           'Проектов уже существует!',
    'subcategories_list_pkey_duplicate': 'Перечень Подкатегорий с указанным ключом уже существует!',

    'coordinates_pkey_duplicate': 'Координаты с указанным ключом уже существуют!',

    'contract_statuses_fullname_key_duplicate': 'Статусы Госконтрактов с указанным наименованием уже существуют!',
    'contract_statuses_pkey_duplicate': 'Статусы Госконтрактов с указанным ключом уже существуют!',

    'construction_progress_unique_duplicate': 'Ход Строительства с указанными ключом и отчетной датой уже существует!',
    'construction_progress_pkey_duplicate': 'Ход Строительства с указанным ключом уже существует!',

    'work_types_fullname_key_duplicate': 'Типы работ с указанным наименованием уже существуют!',
    'work_types_pkey_duplicate': 'Типы работ с указанным ключом уже существуют!',

    'works_list_pkey_duplicate': 'Перечень работ с указанным ключом уже существует!',
    'worklist_unique_duplicate': 'Перечень работ с указанными Объектом Строительства и Типами Конструктивных '
                                 'Элементов уже существует!',
    'works_list_element_types_id_key_duplicate': 'Перечень работ с указанными Типами Конструктивных Элементов уже '
                                                 'существует!',

    'measure_units_pkey_duplicate': 'Единицы измерения с указанным ключом уже существуют!',
    'measure_units_unique_duplicate': 'Единицы измерения с указанными кодом и именем уже существуют!',

    'element_types_fullname_key_duplicate': 'Типы Конструктивных Элементов с указанным наименованием уже существуют!',
    'element_types_pkey_duplicate': 'Типы Конструктивных Элементов с указанным ключом уже существуют!',

    'work_trips_pkey_duplicate': 'Реестр Поездок Руководства МО РФ с указанным ключом уже существует!',

    'visited_objects_pk_duplicate': 'Перечень Посещенных Объектов Строительства с указанными Реестром Поездок '
                                    'Руководства МО РФ и Проектом уже существует!',

    'protocol_pkey_duplicate': 'Протокол с указанным ключом уже существует!',

    'meeting_pkey_duplicate': 'Заседания с указанным ключом уже существуют!',
    'meeting_fullname_key_duplicate': 'Заседания с указанным наименованием уже существуют!',

    'object_documents_pkey_duplicate': 'Документы (Здания и Сооружения) с указанным ключом уже существуют!',
    'object_documents_unique_duplicate': 'Документы (Здания и Сооружения) с указанными Объектом и Документами Проекта '
                                         'уже существует!',

    'doctypes_pkey_duplicate': 'Типы Документов с указанным ключом уже существуют!',
    'doctypes_unique_duplicate': 'Типы Документов с указанными кодом и наименованием уже существуют!',

    'construction_documents_pkey_duplicate': 'Документы Проекта с указанным ключом уже существуют!',

    'organization_documents_pkey_duplicate': 'Документы Организации с указанным ключом уже существуют!',
    'organization_documents_unique_duplicate': 'Документы Организации с указанными Организацией, типом, номером '
                                               'и датой уже существуют!',

    'sortarmedforces_pkey_duplicate': 'Вид ВС с указанным ключом уже существуют!',
    'purposemu_pkey_duplicate': 'Предназначение ВФ с указанным ключом уже существует!',
    'namemilitaryunit_pkey_duplicate': 'Название ВФ с указанным ключом уже существует!',
    'militarycity_pkey_duplicate': 'Военный Городок с указанным ключом уже существует!',
    'keyword_pkey_duplicate': 'Главное Слово с указанным ключом уже существует!',
    'combatarm_pkey_duplicate': 'Род Войск с указанным ключом уже существует!',
    'military_unit_pkey_duplicate': 'Воинское Формирование с указанным ключом уже существует!',

    'organizations_history_ak_duplicate': 'Запись с таким id организации и датой начала уже существует!',
    'officials_pkey_duplicate': 'Должностные лица с указанным ключом уже существуют!',

    'contracts_pkey_duplicate': 'Контракт с указанным ключом уже существует!',
    'contracts_ak_duplicate': 'Контракт с указанным номером и идентификатором уже существует!',
    'contract_worktypes_pkey_duplicate': 'Виды Мероприятий По Гос. Контрактам с указанным ключом уже существуют!',
    'contract_worktypes_fullname_key_duplicate': 'Виды Мероприятий с указанным наименованием уже существуют!',

    'completion_dates_pkey_duplicate': 'Сроки Окончания Работ По Контракту с указанным ключом уже существуют!',
    'completion_dates_unique_duplicate': 'Сроки Окончания Работ По Контракту с указанными Контрактами и '
                                         'Видами Мероприятий уже существуют!',

    'other_duplicate': 'Дубликат записи!',

    'protocol_meetings_type_id_fkey': 'Указанного Типа Заседания не существует!',
    'protocol_idfilestorage_fkey': 'Указанного Файла не существует!',

    'construction_construction_categories_id_fkey': 'Категории Проекта с указанным ключом не существует!',
    'construction_subcategories_list_id_fkey': 'Перечня Подкатегорий Проекта с указанным ключом не существует!',
    'construction_commission_id_fkey': 'Комиссии с указанным ключом не существует!',
    'construction_idMU_fkey': 'Воинского Формирования с указанным ключом не существует!',
    'construction_construction_types_id_fkey': 'Типа Проектов с указанным ключом не существует!',
    'construction_location_types_id_fkey': 'Типа Мест Нахождения Объектов с указанным ключом не существует!',
    'construction_construction_companies_id_fkey': 'Перечня Строительных Организаций с указанным ключом не существует!',
    'construction_oksm_id_fkey': 'ОКСМ с указанным ключом не существует!',
    'construction_coordinates_id_fkey': 'Записи Координат с указанным ключом не существует!',
    'construction_id_fias_fkey': 'ФИАС с указанным ключом не существует!',

    'construction_objects_construction_id_fkey': 'Указанного Проекта не существует!',
    'construction_objects_object_categories_list_id_fkey': 'Указанного Перечня Категорий Объектов не существует!',
    'construction_objects_zones_id_fkey': 'Указанной Зоны Военного Городка не существует!',
    'construction_objects_construction_stages_id_fkey': 'Указанного Этапа Строительства не существует!',
    'construction_objects_coordinates_id_fkey': 'Указанной записи координат не существует!',
    'construction_objects_realty_types_id_fkey': 'Указанных Типов Недвижимости не существует!',

    'object_categories_list_zones_id_fkey': 'Указанной Зоны Военного Городка не существует!',
    'object_categories_list_object_categories_id_fkey': 'Указанной Категории Объекта Строительства не существует!',

    'subcategories_list_construction_categories_id_fkey': 'Указанной Категории Проектов не существует!',
    'subcategories_list_construction_subcategories_id_fkey': 'Указанной Подкатегории Проектов не существует!',

    'work_trips_leadership_positions_id_fkey': 'Указанной Должности не существует!',
    'work_trips_protocol_id_fkey': 'Указанного Протокола не существует!',

    'inspection_objects_construction_id_fkey': 'Указанного Проверенного Объекта Строительства не существует!',
    'inspection_objects_inspections_id_fkey': 'Указанной Проверки Объектов Строительства не существует!',

    'visited_objects_construction_id_fkey': 'Указанного Посещенного Объекта Строительства не существует!',
    'visited_objects_work_trips_id_fkey': 'Указанного Реестра Поездок Руководства МО РФ не существует!',

    'construction_progress_progress_statuses_id_fkey': 'Указанного Статуса Хода Работ не существует!',
    'construction_progress_construction_objects_id_fkey': 'Указанного Объекта Строительства не существует!',

    'works_list_element_types_id_fkey': 'Указанных Типов Конструктивных Элементов не существует!',
    'works_list_unit_id_fkey': 'Указанных Единиц Измерения не существует!',
    'works_list_work_types_id_fkey': 'Указанных Типов Работ не существует!',
    'works_list_construction_objects_id_fkey': 'Указанного Объекта Строительства не существует!',

    'namemilitaryunit_idkeyword_fkey': 'Указанного Главного Слова не существует!',

    'military_unit_pidMU_fkey': 'Указанного Воинского Формирования не существует!',
    'military_unit_idNameMU_fkey': 'Указанного Названия ВФ не существует!',
    'military_unit_idPurpose_fkey': 'Указанного Предназначения ВФ не существует!',
    'military_unit_idMilitaryCity_fkey': 'Указанного Военного Городка не существует!',
    'military_unit_idSortAF_fkey': 'Указанного Вида ВС не существует!',
    'military_unit_idCombatArm_fkey': 'Указанного Рода Войск не существует!',

    'inspection_files_idfilestorage_fkey': 'Указанного Файла не существует!',
    'inspection_files_inspections_id_fkey': 'Указанной Проверки Объектов Строительства не существует!',

    'object_documents_construction_objects_id_fkey': 'Указанного Объекта Строительства не существует!',
    'object_documents_construction_documents_id_fkey': 'Указанных Документов Строительства не существует!',

    'construction_documents_construction_id_fkey': 'Указанного Проекта не существует!',
    'construction_documents_doctypes_id_id_fkey': 'Указанных Типов Документов не существует!',
    'construction_documents_idfilestorage_fkey': 'Указанного Файла не существует!',

    'organizations_parent_organizations_id_fkey': 'Указанной Организации-родителя не существует!',
    'organizations_history_organizations_id_fkey': 'Указанной Организации не существует!',

    'officials_organizations_id_fkey': 'Указанной Организации не существует!',
    'officials_military_ranks_id_fkey': 'Указанного Воинского Звания не существует!',

    'completion_dates_contracts_id_fkey': 'Указанного Контракта не существует!',
    'completion_dates_contract_worktypes_id_fkey': 'Указанных Видов Мероприятий По Гос. Контрактам не существует!',

    'contracts_construction_id_fkey': 'Указанного ИСП не существует!',
    'contracts_contractor_id_fkey': 'Указанного Генерального Подрядчика не существует!',
    'contracts_subcontractor_id_fkey': 'Указанного Субподрядчика не существует!',
    'contracts_contract_statuses_id_fkey': 'Указанного Статуса Контракта не существует!',

    'other_fkey': 'Вторичный ключ не найден!',

    'contract_nf': 'Указанного контракта не существует!',
    'contract_work_type_nf': 'Указанных Видов Мероприятий По Государственным Контрактам не существует!',

    'completion_date_nf': 'Указанных Сроков Окончания Работ По Контракту не существует!',

    'organization_nf': 'Указанной Организации не существует!',
    'organization_history_nf': 'Указанный реквизит не найден!',
    'organization_history_delete_limit': 'Нельзя удалить единственный реквизит!'

}
