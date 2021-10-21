from .model import ConstructionSubcategory
from .repository import ConstructionSubcategoryRepository


class ConstructionSubcategoryService:

    def __init__(self):
        self.repo = ConstructionSubcategoryRepository()

    def get_all_construction_subcategories(self) -> list:
        return self.repo.get_all_construction_subcategories()

    def get_many_construction_subcategories_by_id(self, ids: list) -> list:
        return self.repo.get_many_construction_subcategories_by_id(ids)

    def get_construction_subcategory_by_id(self, id: int) -> ConstructionSubcategory:
        return self.repo.get_construction_subcategory_by_id(id)

    def add_construction_subcategory(self, construction_subcategory: ConstructionSubcategory) -> None:
        self.repo.add_construction_subcategory(construction_subcategory)

    def delete_construction_subcategory_by_id(self, id: int) -> None:
        self.repo.delete_construction_subcategory_by_id(id)

    def update_construction_subcategory(self, construction_subcategory: ConstructionSubcategory) -> None:
        self.repo.update_construction_subcategory(construction_subcategory)