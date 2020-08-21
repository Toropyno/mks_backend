import colander

from mks_backend.controllers.schemas.validator_utils import construction_category_validator
from mks_backend.controllers.schemas.validator_utils import construction_subcategory_validator


class SubcategoriesListSchema(colander.MappingSchema):
    construction_categories_id = colander.SchemaNode(
        colander.Integer(),
        name='constructionCategoriesId',
        validator=construction_category_validator
    )

    construction_subcategories_id = colander.SchemaNode(
        colander.Integer(),
        name='constructionSubcategoriesId',
        validator=construction_subcategory_validator
    )
