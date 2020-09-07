from mks_backend.models.construction_subcategory import ConstructionSubcategory
from mks_backend.repositories.construction_subcategory_repository import ConstructionSubcategoryRepository


class ConstructionSubcategoryService:

    def __init__(self):
        self.repo = ConstructionSubcategoryRepository()

    def get_all_construction_subcategories(self) -> list:
        return self.repo.get_all_construction_subcategories()

    def get_construction_subcategory_by_id(self, id: int) -> ConstructionSubcategory:
        return self.repo.get_construction_subcategory_by_id(id)

    def add_construction_subcategory(self, construction_subcategory: ConstructionSubcategory) -> None:
        self.repo.add_construction_subcategory(construction_subcategory)

    def delete_construction_subcategory_by_id(self, id: int) -> None:
        self.repo.delete_construction_subcategory_by_id(id)

    def update_construction_subcategory(self, construction_subcategory: ConstructionSubcategory) -> None:
        self.repo.update_construction_subcategory(construction_subcategory)
