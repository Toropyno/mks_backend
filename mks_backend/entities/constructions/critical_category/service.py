
from .model import CriticalCategory
from .repository import CriticalCategoryRepository


class CriticalCategoryService:

    def __init__(self):
        self.repo = CriticalCategoryRepository()

    def get_critical_category_by_id(self, id: int) -> CriticalCategory:
        return self.repo.get_critical_category_by_id(id)

    def add_critical_category(self, critical_category: CriticalCategory) -> None:
        self.repo.add_critical_category(critical_category)

    def delete_critical_category_by_id(self, id: int) -> None:
        self.repo.delete_critical_category_by_id(id)

    def update_critical_category(self, critical_category: CriticalCategory) -> None:
        self.repo.update_critical_category(critical_category)

    def get_all_construction_categories(self) -> list:
        return self.repo.get_all_critical_category()
