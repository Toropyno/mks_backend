import colander

from mks_backend.controllers.schemas.validator_utils import strip_space


class ConstructionStagesSchema(colander.MappingSchema):

    code = colander.SchemaNode(
        colander.String(allow_empty=True),
        name='code',
        preparer=[strip_space],
        validator=colander.Length(
            min=1,
            max=20,
            min_err='Слишком короткое краткое наименование',
            max_err='Слишком длинное краткое наименование'
        )
    )

    fullname = colander.SchemaNode(
        colander.String(allow_empty=True),
        name='fullName',
        preparer=[strip_space],
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое полное наименование',
            max_err='Слишком длинное полное наименование'
        )
    )
