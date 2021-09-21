from .model import ObjectCategoryList
from .repository import ObjectCategoryListRepository


class ObjectCategoryListService:

    def __init__(self):
        self.repo = ObjectCategoryListRepository()

    def get_all_object_categories_lists(self) -> list:
        return self.repo.get_all_object_categories_lists()

    def get_object_categories_list_by_id(self, id: int) -> ObjectCategoryList:
        return self.repo.get_object_categories_list_by_id(id)

    def get_object_categories_list_by_relations(self, zone_id, object_category_id) -> ObjectCategoryList:
        return self.repo.get_object_categories_list_by_relations(zone_id, object_category_id)
