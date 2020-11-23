import colander

from mks_backend.controllers.schemas.validator_utils import date_validator, strip_space


class WorkListSchema(colander.MappingSchema):

    construction_object_id = colander.SchemaNode(
        colander.Integer(),
        name='constructionObject'
    )

    element_type_id = colander.SchemaNode(
        colander.Integer(),
        name='element'
    )

    weight = colander.SchemaNode(
        colander.Integer(),
        name='weight',
        validator=colander.Range(
            min=1,
            max=100,
            min_err='Слишком малый вес элемента',
            max_err='Слишком большой вес элемента'
        )
    )

    element_description = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='elementDescription',
        validator=colander.Length(
            min=1,
            max=500,
            max_err='Слишком длинное описание элемента'
        ),
        missing=None
    )

    begin_date = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='beginDate',
        validator=date_validator
    )

    end_date = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='endDate',
        validator=date_validator
    )

    measure_unit = colander.SchemaNode(
        colander.Integer(),
        name='measureUnit'
    )

    plan = colander.SchemaNode(
        colander.Decimal(1),
        name='plan',
        validator=colander.Range(
            min=0.1,
            max=100,
            min_err='Показатель запланированного выполнения работ не может быть меньше 0%',
            max_err='Показатель запланированного выполнения работ не может быть больше 100%'
        )
    )

    fact = colander.SchemaNode(
        colander.Decimal(1),
        name='fact',
        validator=colander.Range(
            min=0.1,
            max=100,
            min_err='Показатель фактического выполнения работ не может быть меньше 0%',
            max_err='Показатель фактического выполнения работ не может быть больше 100%'
        )
    )

    work_type_id = colander.SchemaNode(
        colander.Integer(),
        name='workType',
        missing=None
    )

    work_description = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='workDescription',
        validator=colander.Length(
            max=500,
            max_err='Слишком длинное описание работы'
        ),
        missing=None
    )

    note = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='note',
        validator=colander.Length(
            max=1000,
            max_err='Слишком длинное примечание к работе'
        ),
        missing=None
    )

    relevance_date = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='relevanceDate',
        validator=date_validator
    )

