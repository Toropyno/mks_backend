import colander

from mks_backend.utils.validator_utils import date_validator, organization_uuid, strip_space


class ConstructionSchema(colander.MappingSchema):
    project_code = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='code',
        validator=colander.Length(
            min=1,
            max=40,
            min_err='Слишком короткий код проекта',
            max_err='Слишком длинный код проекта'
        )
    )

    project_name = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='name',
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое имя проекта',
            max_err='Слишком длинное имя проекта'
        )
    )

    construction_categories_id = colander.SchemaNode(
        colander.Int(),
        name='category',
        validator=colander.Range(
            min=0,
            min_err='Неверный номер категории'
        ),
        missing=None
    )

    subcategories_list_id = colander.SchemaNode(
        colander.Int(),
        name='subcategory',
        validator=colander.Range(
            min=0,
            min_err='Неверный номер подкатегории'
        ),
        missing=None
    )

    is_critical = colander.SchemaNode(
        colander.Bool(),
        name='isCritical',
        validator=colander.OneOf([True, False])
    )

    commission_id = colander.SchemaNode(
        colander.Int(),
        name='commission',
        validator=colander.Range(
            min=0,
            min_err='Неверный номер комиссии'
        )
    )

    idMU = colander.SchemaNode(
        colander.Int(),
        name='militaryUnit',
        validator=colander.Range(
            min=0,
            min_err='Неверный номер воинского формирования'
        ),
        missing=None
    )

    object_amount = colander.SchemaNode(
        colander.Int(),
        name='objectsAmount',
        validator=colander.Range(
            min=1,
            min_err='Неверное кол-во объектов'
        )
    )

    department = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='department',
        validator=colander.Length(
            max=255,
            max_err='Слишком длинное наименование отдела'
        ),
        missing=None
    )

    officer = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='officer',
        validator=colander.Length(
            max=100,
            max_err='Слишком длинное имя ответственного лица'
        ),
        missing=None
    )

    technical_spec = colander.SchemaNode(
        colander.Bool(false_choices=['false', '0', 'False', 'none']),
        name='technicalSpec',
    )

    price_calc = colander.SchemaNode(
        colander.Bool(false_choices=['false', '0', 'False', 'none']),
        name='priceCalc',
    )

    deletion_mark = colander.SchemaNode(
        colander.Bool(false_choices=['false', '0', 'False', 'none']),
        name='deletionMark',
    )

    # ------ coordinate ------

    latitude = colander.SchemaNode(
        colander.Float(),
        name='latitude',
        validator=colander.Range(
            min=-90,
            min_err='Недопустимые координаты объекта',
            max=90,
            max_err='Недопустимые координаты объекта',
        ),
        missing=None
    )

    longitude = colander.SchemaNode(
        colander.Float(),
        name='longitude',
        validator=colander.Range(
            min=-180,
            min_err='Недопустимые координаты объекта',
            max=180,
            max_err='Недопустимые координаты объекта',
        ),
        missing=None
    )

    zoom = colander.SchemaNode(
        colander.Int(),
        name='zoom',
        validator=colander.Range(
            min=1,
            min_err='Недопустимая степень приближения',
            max=23,
            max_err='Недопустимая степень приближения',
        ),
        missing=None
    )

    coordinate_id = colander.SchemaNode(
        colander.Int(),
        name='coordinateId',
        validator=colander.Range(
            min=0,
            min_err='Недопустимое местоположение'
        ),
        missing=None
    )

    # ----------------------

    construction_types_id = colander.SchemaNode(
        colander.Int(),
        name='constructionType',
        validator=colander.Range(
            min=0,
            min_err='Такого типа проекта не существует'
        ),
        missing=None
    )

    location_types_id = colander.SchemaNode(
        colander.Int(),
        name='locationType',
        validator=colander.Range(
            min=0,
            min_err='Такого типа местоположения не существует'
        ),
        missing=None
    )

    construction_companies_id = colander.SchemaNode(
        colander.Int(),
        name='constructionCompany',
        validator=colander.Range(
            min=0,
            min_err='Такой компании не существует'
        )
    )

    oksm_id = colander.SchemaNode(
        colander.Int(),
        name='oksm',
        validator=colander.Range(
            min=0,
            min_err='Такой записи в ОКСМ не существует'
        ),
        missing=None
    )

    id_fias = colander.SchemaNode(
        colander.Int(),
        name='fias',
        validator=colander.Range(
            min=0,
            min_err='Такой записи не существует в ФИАС'
        ),
        missing=None
    )

    address = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='address',
        validator=colander.Length(
            max=1000,
            max_err='Слишком длинный адрес'
        ),
        missing=None
    )

    note = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='note',
        validator=colander.Length(
            max=1000,
            max_err='Слишком длинное примечание'
        ),
        missing=None
    )

    organizations_id = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='organization',
        validator=organization_uuid,
        missing=None
    )

    military_district = colander.SchemaNode(
        colander.Int(),
        name='militaryDistrict',
        validator=colander.Range(
            min=1,
            min_err='Неверный номер военного округа'
        ),
        missing=colander.drop
    )

    construction_critical_categories_id = colander.SchemaNode(
        colander.Int(),
        name='criticalCategory',
        validator=colander.Range(
            min=0,
            min_err='Такой категории критичных объектов не существует'
        ),
        missing=None
    )

    # TODO: remove when FIAS will be ok
    region = colander.SchemaNode(colander.String(), name='region', missing=colander.drop)
    area = colander.SchemaNode(colander.String(), name='area', missing=colander.drop)
    city = colander.SchemaNode(colander.String(), name='city', missing=colander.drop)
    settlement = colander.SchemaNode(colander.String(), name='settlement', missing=colander.drop)
    street = colander.SchemaNode(colander.String(), name='street', missing=colander.drop)


class ConstructionFilterSchema(colander.MappingSchema):
    project_code = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='code',
        validator=colander.Length(
            min=1,
            max=40,
            min_err='Слишком короткий код проекта',
            max_err='Слишком длинный код проекта'
        ),
        missing=colander.drop
    )

    project_name = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='name',
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое имя проекта',
            max_err='Слишком длинное имя проекта'
        ),
        missing=colander.drop
    )

    construction_categories_id = colander.SchemaNode(
        colander.Int(),
        name='category',
        validator=colander.Range(
            min=1,
            min_err='Неверный номер категории'
        ),
        missing=colander.drop
    )

    subcategories_list_id = colander.SchemaNode(
        colander.Int(),
        name='subcategory',
        validator=colander.Range(
            min=1,
            min_err='Неверный номер подкатегории'
        ),
        missing=colander.drop
    )

    is_critical = colander.SchemaNode(
        colander.Bool(),
        name='isCritical',
        validator=colander.OneOf([True, False]),
        missing=colander.drop
    )

    commission_id = colander.SchemaNode(
        colander.Int(),
        name='commission',
        validator=colander.Range(
            min=1,
            min_err='Неверный номер комиссии'
        ),
        missing=colander.drop
    )

    idMU = colander.SchemaNode(
        colander.Int(),
        name='militaryUnit',
        validator=colander.Range(
            min=1,
            min_err='Неверный номер воинского формирования'
        ),
        missing=colander.drop
    )

    object_amount = colander.SchemaNode(
        colander.Int(),
        name='objectsAmount',
        validator=colander.Range(
            min=1,
            min_err='Неверное кол-во объектов'
        ),
        missing=colander.drop
    )

    planned_date_start = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='plannedDateStart',
        validator=date_validator,
        missing=colander.drop
    )

    planned_date_end = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='plannedDateEnd',
        validator=date_validator,
        missing=colander.drop
    )

    oksm = colander.SchemaNode(
        colander.String(),
        name='oksm',
        missing=colander.drop
    )

    region = colander.SchemaNode(
        colander.String(),
        name='region',
        missing=colander.drop
    )

    area = colander.SchemaNode(
        colander.String(),
        name='area',
        missing=colander.drop
    )

    city = colander.SchemaNode(
        colander.String(),
        name='city',
        missing=colander.drop
    )

    settlement = colander.SchemaNode(
        colander.String(),
        name='settlement',
        missing=colander.drop
    )

    location_type = colander.SchemaNode(
        colander.Integer(),
        name='locationType',
        missing=colander.drop
    )

    company = colander.SchemaNode(
        colander.Integer(),
        name='company',
        missing=colander.drop
    )

    organization_id = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='organization',
        validator=organization_uuid,
        missing=colander.drop
    )

    readiness = colander.SchemaNode(
        colander.Integer(),
        name='readiness',
        validator=colander.Range(
            min=0,
            max=100,
            min_err='Процент готовности не может быть меньше нуля',
            max_err='Процент готовности не может быть больше сотни'
        ),
        missing=colander.drop
    )

    deletion_mark = colander.SchemaNode(
        colander.Boolean(false_choices=['false', '0', 'False', 'none']),
        name='deletionMark',
        missing=colander.drop
    )

    military_district = colander.SchemaNode(
        colander.Int(),
        name='militaryDistrict',
        validator=colander.Range(
            min=1,
            min_err='Неверный номер военного округа'
        ),
        missing=colander.drop
    )

    critical_category = colander.SchemaNode(
        colander.Int(),
        name='criticalCategory',
        validator=colander.Range(
            min=0,
            min_err='Такой категории критичных объектов не существует'
        ),
        missing=colander.drop
    )
