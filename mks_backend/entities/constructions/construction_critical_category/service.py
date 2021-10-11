
from .model import ConstructionCriticalCategory
from .repository import ConstructionCriticalCategoryRepository


class ConstructionCriticalCategoryService:

    def __init__(self):
        self.repo = ConstructionCriticalCategoryRepository()

    def get_construction_critical_category_by_id(self, id: int) -> ConstructionCriticalCategory:
        return self.repo.get_construction_critical_category_by_id(id)

    def add_construction_critical_category(self, construction_critical_category: ConstructionCriticalCategory) -> None:
        self.repo.add_construction_critical_category(construction_critical_category)

    def delete_construction_critical_category_by_id(self, id: int) -> None:
        self.repo.delete_construction_critical_category_by_id(id)

    def update_construction_critical_category(self, construction_critical_category: ConstructionCriticalCategory) -> None:
        self.repo.update_construction_critical_category(construction_critical_category)

    def get_all_construction_categories(self) -> list:
        return self.repo.get_all_construction_critical_categories()
