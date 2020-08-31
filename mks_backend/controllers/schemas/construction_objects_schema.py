import colander

from mks_backend.controllers.schemas.validator_utils import date_validator, strip_space


class ConstructionObjectsSchema(colander.MappingSchema):

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
