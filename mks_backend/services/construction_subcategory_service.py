from mks_backend.models.construction_subcategories import ConstructionSubcategories
from mks_backend.repositories.construction_subcategories_repository import ConstructionSubcategoryRepository


class ConstructionSubcategoriesService:

    def __init__(self):
        self.repo = ConstructionSubcategoryRepository()

    def get_all_construction_subcategories(self) -> list:
        return self.repo.get_all_construction_subcategories()

    def get_construction_subcategory_by_id(self, id: int) -> ConstructionSubcategories:
        return self.repo.get_construction_subcategory_by_id(id)

    def add_construction_subcategory(self, construction_subcategory: ConstructionSubcategories) -> None:
        self.repo.add_construction_subcategory(construction_subcategory)

    def delete_construction_subcategory_by_id(self, id: int) -> None:
        self.repo.delete_construction_subcategory_by_id(id)

    def update_construction_subcategory(self, construction_subcategory: ConstructionSubcategories) -> None:
        self.repo.update_construction_subcategory(construction_subcategory)
