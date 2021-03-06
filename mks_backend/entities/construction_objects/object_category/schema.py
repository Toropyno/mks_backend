import colander

from mks_backend.utils.validator_utils import strip_space


class ObjectCategorySchema(colander.MappingSchema):
    fullname = colander.SchemaNode(
        colander.String(),
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
        colander.String(),
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
