import colander

from mks_backend.utils.validator_utils import strip_space


class ZoneSchema(colander.MappingSchema):
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

    categories = colander.SchemaNode(
        colander.List(),
        missing=None
    )
