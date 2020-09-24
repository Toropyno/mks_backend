import colander

from mks_backend.controllers.schemas.validator_utils import date_validator, strip_space


class ConstructionObjectSchema(colander.MappingSchema):

    construction_id = colander.SchemaNode(
        colander.Int(),
        name='projectId',
        validator=colander.Range(
            min=0,
            min_err='Недопустимое значение ИСП'
        )
    )

    object_code = colander.SchemaNode(
        colander.String(),
        name='code',
        preparer=[strip_space],
        validator=colander.Length(
            min=1,
            max=40,
            min_err='Слишком короткий код проекта',
            max_err='Слишком длинный код проекта'
        )
    )

    object_name = colander.SchemaNode(
        colander.String(),
        name='name',
        preparer=[strip_space],
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое наименование',
            max_err='Слишком длинное наименование'
        )

    )

    zones_id = colander.SchemaNode(
        colander.Int(),
        name='zone',
        validator=colander.Range(
            min=0,
            min_err='Недопустимое значение зоны'
        ),
        missing=None
    )

    object_categories_list_id = colander.SchemaNode(
        colander.Int(),
        name='category',
        validator=colander.Range(
            min=0,
            min_err='Недопустимое значение перечня категорий объектов'
        ),
        missing=None
    )

    planned_date = colander.SchemaNode(
        colander.String(),
        name='plannedDate',
        preparer=[strip_space],
        validator=date_validator
    )

    weight = colander.SchemaNode(
        colander.Int(),
        name='weight',
        validator=colander.Range(
            min=0,
            max=100,
            min_err='Вес объекта не может быть отрицательным',
            max_err='Слишком большой вес объекта'
        )
    )

    generalplan_number = colander.SchemaNode(
        colander.Int(),
        name='generalPlanNumber',
        validator=colander.Range(
            min=0,
            min_err='Недопустимый номер объекта на генеральном плане'
        ),
        missing=None
    )

    building_volume = colander.SchemaNode(
        colander.Decimal(),
        name='buildingVolume',
        validator=colander.Range(
            min=1,
            min_err='Недопустимый объем здания'
        ),
        missing=None
    )

    floors_amount = colander.SchemaNode(
        colander.Int(),
        name='floorsAmount',
        validator=colander.Range(
            min=1,
            min_err='Недопустимое количество этажей'
        ),
        missing=None
    )

    construction_stages_id = colander.SchemaNode(
        colander.Int(),
        name='stage',
        validator=colander.Range(
            min=0,
            min_err='Недопустимый этап строительства'
        ),
        missing=None
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

    location_id = colander.SchemaNode(
        colander.Int(),
        name='locationId',
        validator=colander.Range(
            min=0,
            min_err='Недопустимое местоположение'
        ),
        missing=None
    )

    # realty_types_id = colander.SchemaNode(
    #     colander.Int(),
    #     name='realtyTypeId',
    #     validator=colander.Range(
    #         min=0,
    #         min_err='Недопустимое значение типа недвижимости'
    #     ),
    #     missing=None
    # )

    fact_date = colander.SchemaNode(
        colander.String(),
        name='factDate',
        preparer=[strip_space],
        validator=date_validator,
        missing=None
    )
