import colander

from mks_backend.utils.validator_utils import strip_space


class WorkTypeSchema(colander.MappingSchema):
    fullname = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='fullName',
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое наименование типа работы',
            max_err='Слишком длинное наименование типа работы'
        )
    )

    note = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='note',
        validator=colander.Length(
            max=1000,
            max_err='Слишком длинное примечание для типа работы'
        ),
        missing=None
    )
