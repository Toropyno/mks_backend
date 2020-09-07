from mks_backend.models.subcategories_list import SubcategoriesList
from mks_backend.repositories.subcategories_list_repository import SubcategoriesListRepository


class SubcategoriesListService:

    def __init__(self):
        self.repo = SubcategoriesListRepository()

    def get_subcategories_list_by_id(self, id: int) -> SubcategoriesList:
        return self.repo.get_subcategories_list_by_id(id)

    def add_subcategories_list(self, subcategories_list: SubcategoriesList) -> None:
        return self.repo.add_subcategories_list(subcategories_list)

    def delete_subcategories_list_by_id(self, id: int) -> None:
        self.repo.delete_subcategories_list_by_id(id)

    def get_all_subcategories_lists(self) -> list:
        return self.repo.get_all_subcategories_lists()
