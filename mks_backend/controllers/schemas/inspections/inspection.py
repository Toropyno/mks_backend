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
