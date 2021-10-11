import colander

from mks_backend.utils.validator_utils import strip_space


class ConstructionCriticalCategorySchema(colander.MappingSchema):
    id = colander.SchemaNode(
        colander.Integer(),
        name='id',
        missing=None
    )

    fullname = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='fullName',
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое наименование критичной категории',
            max_err='Слишком длинное наименование критичной категории'
        )
    )
