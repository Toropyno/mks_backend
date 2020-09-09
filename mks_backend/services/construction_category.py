from mks_backend.models.construction_category import ConstructionCategory
from mks_backend.repositories.construction_category import ConstructionCategoryRepository


class ConstructionCategoryService:

    def __init__(self):
        self.repo = ConstructionCategoryRepository()

    def get_construction_category_by_id(self, id: int) -> ConstructionCategory:
        return self.repo.get_construction_category_by_id(id)

    def add_construction_category(self, construction_categories: ConstructionCategory) -> None:
        self.repo.add_construction_category(construction_categories)

    def delete_construction_category_by_id(self, id: int) -> None:
        self.repo.delete_construction_category_by_id(id)

    def update_construction_category(self, construction_category: dict) -> None:
        self.repo.update_construction_category(construction_category)

    def get_all_construction_categories(self) -> list:
        return self.repo.get_all_construction_categories()
