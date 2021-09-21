import colander

from mks_backend.utils.validator_utils import strip_space


class LeadershipPositionSchema(colander.MappingSchema):
    code = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='code',
        validator=colander.Length(
            max=25,
            max_err='Слишком длинный код для должности'
        )
    )

    fullname = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='fullName',
        validator=colander.Length(
            max=255,
            max_err='Слишком длинное наименование должности'
        )
    )
