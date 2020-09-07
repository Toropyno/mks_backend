from mks_backend.models.object_categories_list import ObjectCategoriesList
from mks_backend.repositories.object_categories_lists_repository import ObjectCategoriesListRepository


class ObjectCategoriesListService:

    def __init__(self):
        self.repo = ObjectCategoriesListRepository()

    def get_all_object_categories_lists(self) -> list:
        return self.repo.get_all_object_categories_lists()

    def get_object_categories_list_by_id(self, id: int) -> ObjectCategoriesList:
        return self.repo.get_object_categories_list_by_id(id)

    def add_object_categories_list(self, object_categories_list: ObjectCategoriesList) -> None:
        self.repo.add_object_categories_list(object_categories_list)

    def delete_object_categories_list_by_id(self, id: int) -> None:
        self.repo.delete_object_categories_list_by_id(id)

    def update_object_categories_list(self, new_object_categories_list: ObjectCategoriesList) -> None:
        self.repo.update_object_categories_list(new_object_categories_list)
