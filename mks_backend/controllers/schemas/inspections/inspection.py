import colander

from mks_backend.controllers.schemas.validator_utils import date_validator, strip_space


class InspectionSchema(colander.MappingSchema):

    inspection_date = colander.SchemaNode(
        colander.String(),
        name='date',
        validator=date_validator
    )

    inspection_name = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='name',
        validator=colander.Length(
            max=255,
            max_err='Слишком длинное наименование проверки'
        )
    )

    inspector = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='inspector',
        validator=colander.Length(
            max=100,
            max_err='Слишком длинное имя руководителя проверки'
        )
    )

    insp_result = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='result',
        validator=colander.Length(
            max=2000,
            max_err='Слишком длинный результат проверки'
        ),
        missing=None
    )


class InspectionFilterSchema(colander.MappingSchema):

    date_start = colander.SchemaNode(
        colander.String(),
        name='dateStart',
        validator=date_validator,
        missing=colander.drop
    )

    date_end = colander.SchemaNode(
        colander.String(),
        name='dateEnd',
        validator=date_validator,
        missing=colander.drop
    )

    inspection_name = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='name',
        validator=colander.Length(
            max=255,
            max_err='Слишком длинное наименование проверки'
        ),
        missing=colander.drop
    )

    inspector = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='inspector',
        validator=colander.Length(
            max=100,
            max_err='Слишком длинное имя руководителя проверки'
        ),
        missing=colander.drop
    )

    have_file = colander.SchemaNode(
        colander.Boolean(),
        name='haveFile',
        missing=colander.drop
    )

    have_inspected_objects = colander.SchemaNode(
        colander.Boolean(),
        name='haveInspectedObjects',
        missing=colander.drop
    )

    construction_code = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='constructionCode',
        validator=colander.Length(
            max=40,
            max_err='Слишком длинный код проекта'
        ),
        missing=colander.drop
    )

    is_critical = colander.SchemaNode(
        colander.Bool(),
        name='isCritical',
        missing=colander.drop
    )

    # TODO: add FIAS Subject field
