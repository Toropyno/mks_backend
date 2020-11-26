from mks_backend.models.constructions import SubcategoryList
from mks_backend.repositories.constructions.subcategory_list import SubcategoryListRepository


class SubcategoryListService:

    def __init__(self):
        self.repo = SubcategoryListRepository()

    def get_subcategories_list_by_id(self, id: int) -> SubcategoryList:
        return self.repo.get_subcategories_list_by_id(id)

    def add_subcategories_list(self, subcategories_list: SubcategoryList) -> None:
        return self.repo.add_subcategories_list(subcategories_list)

    def delete_subcategories_list_by_id(self, id: int) -> None:
        self.repo.delete_subcategories_list_by_id(id)

    def get_all_subcategories_lists(self) -> list:
        return self.repo.get_all_subcategories_lists()

    def get_subcategories_list_by_relations(self, category_id, subcategory_id):
        return self.repo.get_subcategories_list_by_relations(category_id, subcategory_id)
