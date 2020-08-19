import colander

from mks_backend.controllers.schemas.validator_utils import strip_space


class ObjectCategorySchema(colander.MappingSchema):

    fullname = colander.SchemaNode(
        colander.String(allow_empty=True),
        name='fullName',
        preparer=[strip_space],
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое наименование',
            max_err='Слишком длинное наименование'
        )
    )

    note = colander.SchemaNode(
        colander.String(allow_empty=True),
        name='note',
        preparer=[strip_space],
        validator=colander.Length(
            min=1,
            max=1000,
            min_err='Слишком короткое наименование',
            max_err='Слишком длинное наименование'
        ),
        missing=None
    )