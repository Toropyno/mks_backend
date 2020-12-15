import colander

from mks_backend.controllers.schemas.validator_utils import strip_space


class DocTypeSchema(colander.MappingSchema):
    code = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='code',
        validator=colander.Length(
            min=1,
            max=40,
            min_err='Слишком короткий код типа документа',
            max_err='Слишком длинный код типа документа'
        )
    )

    fullname = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='fullName',
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое наименование типа документа',
            max_err='Слишком длинное наименование типа документа'
        )
    )
