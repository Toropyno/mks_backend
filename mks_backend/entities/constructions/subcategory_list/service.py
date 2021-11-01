from .model import SubcategoryList
from .repository import SubcategoryListRepository


class SubcategoryListService:

    def __init__(self):
        self.repo = SubcategoryListRepository()

    def get_subcategories_list_by_id(self, id_: int) -> SubcategoryList:
        return self.repo.get_subcategories_list_by_id(id_)

    def add_subcategories_list(self, subcategories_list: SubcategoryList) -> None:
        return self.repo.add_subcategories_list(subcategories_list)

    def delete_subcategories_list_by_id(self, id_: int) -> None:
        self.repo.delete_subcategories_list_by_id(id_)

    def get_all_subcategories_lists(self) -> list:
        return self.repo.get_all_subcategories_lists()

    def get_subcategories_list_by_relations(self, category_id, subcategory_id):
        return self.repo.get_subcategories_list_by_relations(category_id, subcategory_id)
