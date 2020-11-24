from mks_backend.models.constructions import ConstructionCategory
from mks_backend.repositories.constructions.construction_category import ConstructionCategoryRepository
from mks_backend.services.constructions.construction_subcategory import ConstructionSubcategoryService


class ConstructionCategoryService:

    def __init__(self):
        self.repo = ConstructionCategoryRepository()
        self.subcategory_service = ConstructionSubcategoryService()

    def get_construction_category_by_id(self, id: int) -> ConstructionCategory:
        return self.repo.get_construction_category_by_id(id)

    def add_construction_category(self, construction_category: ConstructionCategory) -> None:
        self.repo.add_construction_category(construction_category)

    def delete_construction_category_by_id(self, id: int) -> None:
        self.repo.delete_construction_category_by_id(id)

    def update_construction_category(self, construction_category: ConstructionCategory) -> None:
        self.repo.update_construction_category(construction_category)

    def get_all_construction_categories(self) -> list:
        return self.repo.get_all_construction_categories()

    def convert_schema_to_object(self, schema: dict) -> ConstructionCategory:
        category_id = schema.get('id')
        if category_id:
            category = self.get_construction_category_by_id(category_id)
        else:
            category = ConstructionCategory()

        subcategories = schema.get('subcategory', [])
        if subcategories is not None:
            subcategories_ids = list(map(lambda x: x['id'], subcategories))
            category.subcategories = self.subcategory_service.get_many_construction_subcategories_by_id(
                subcategories_ids
            )

        category.fullname = schema.get('fullName')
        return category
