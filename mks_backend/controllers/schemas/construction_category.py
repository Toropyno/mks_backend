import colander

from mks_backend.controllers.schemas.validator_utils import strip_space


class ConstructionCategorySchema(colander.MappingSchema):
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
            min_err='Слишком короткое наименование объекта',
            max_err='Слишком длинное наименование объекта'
        )
    )

    subcategory = colander.SchemaNode(
        colander.List(),
        missing=None
    )
