import colander

from mks_backend.controllers.schemas.validator_utils import date_validator


class ConstructionSchema(colander.MappingSchema):
    project_code = colander.SchemaNode(
        colander.String(),
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

    contract_date = colander.SchemaNode(
        colander.String(),
        name='contractDate',
        validator=date_validator
    )

    object_amount = colander.SchemaNode(
        colander.Int(),
        name='objectsAmount',
        validator=colander.Range(
            min=1,
            min_err='Неверное кол-во объектов'
        )
    )

    planned_date = colander.SchemaNode(
        colander.String(),
        name='plannedDate',
        validator=date_validator
    )

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

class ConstructionFilterSchema(colander.MappingSchema):
    project_code = colander.SchemaNode(
        colander.String(),
        name='code',
        validator=colander.Length(
            min=1,
            max=40,
            min_err='Слишком короткий код проекта',
            max_err='Слишком длинный код проекта'
        ),
        missing=None
    )

    project_name = colander.SchemaNode(
        colander.String(),
        name='name',
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое имя проекта',
            max_err='Слишком длинное имя проекта'
        ),
        missing=None
    )

    construction_categories_id = colander.SchemaNode(
        colander.Int(),
        name='category',
        validator=colander.Range(
            min=1,
            min_err='Неверный номер категории'
        ),
        missing=None
    )

    subcategories_list_id = colander.SchemaNode(
        colander.Int(),
        name='subcategory',
        validator=colander.Range(
            min=1,
            min_err='Неверный номер подкатегории'
        ),
        missing=None
    )

    is_critical = colander.SchemaNode(
        colander.Bool(),
        name='isCritical',
        validator=colander.OneOf([True, False]),
        missing=None
    )

    commission_id = colander.SchemaNode(
        colander.Int(),
        name='commission',
        validator=colander.Range(
            min=1,
            min_err='Неверный номер комиссии'
        ),
        missing=None
    )

    idMU = colander.SchemaNode(
        colander.Int(),
        name='militaryUnit',
        validator=colander.Range(
            min=1,
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
        ),
        missing=None
    )

    contract_date_start = colander.SchemaNode(
        colander.String(),
        name='contractDateStart',
        validator=date_validator,
        missing=None
    )

    contract_date_end = colander.SchemaNode(
        colander.String(),
        name='contractDateEnd',
        validator=date_validator,
        missing=None
    )

    planned_date_start = colander.SchemaNode(
        colander.String(),
        name='plannedDateStart',
        validator=date_validator,
        missing=None
    )

    planned_date_end = colander.SchemaNode(
        colander.String(),
        name='plannedDateEnd',
        validator=date_validator,
        missing=None
    )
