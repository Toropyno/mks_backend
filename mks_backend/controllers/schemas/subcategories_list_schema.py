import colander

from mks_backend.controllers.construction_controller import construction_category_validator
from mks_backend.controllers.construction_controller import construction_subcategory_validator
from mks_backend.repositories.construction_categories_repository import ConstructionCategoryRepository
from mks_backend.repositories.construction_subcategories_repository import ConstructionSubcategoryRepository


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


def construction_category_validator(node, value):
    if not ConstructionCategoryRepository.get_construction_category_by_id(value):
        raise colander.Invalid(node, 'Такой категории для проекта не существует')


def construction_subcategory_validator(node, value):
    if not ConstructionSubcategoryRepository.get_construction_subcategory_by_id(value):
        raise colander.Invalid(node, 'Такой подкатегории для проекта не существует')
