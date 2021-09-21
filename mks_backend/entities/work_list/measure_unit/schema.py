import colander

from mks_backend.utils.validator_utils import strip_space


class MeasureUnitSchema(colander.MappingSchema):
    unit_code = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='code',
        validator=colander.Length(
            min=1,
            max=20,
            min_err='Слишком короткий код единиц измерения',
            max_err='Слишком длинный код единиц измерения'
        )
    )

    unit_name = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='name',
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое наименование единиц измерения',
            max_err='Слишком длинное наименование единиц измерения'
        )
    )
