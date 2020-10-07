from mks_backend.models.object_category_list import ObjectCategoryList
from mks_backend.models.object_file import ObjectFile
from mks_backend.repositories.object_category_list import ObjectCategoryListRepository


class ObjectCategoryListService:

    def __init__(self):
        self.repo = ObjectCategoryListRepository()

    def get_all_object_categories_lists(self) -> list:
        return self.repo.get_all_object_categories_lists()

    def get_object_categories_list_by_id(self, id: int) -> ObjectCategoryList:
        return self.repo.get_object_categories_list_by_id(id)

    def get_object_categories_list_by_relations(self, zone_id, object_category_id) -> ObjectCategoryList:
        return self.repo.get_object_categories_list_by_relations(zone_id, object_category_id)

    def get_all_object_files(self) -> list:
        return self.repo.get_all_object_files()

    def get_object_file_by_id(self, id: int) -> ObjectFile:
        return self.repo.get_object_file_by_id(id)

    def add_object_file(self, object_file: ObjectFile) -> None:
        self.repo.add_object_file(object_file)

    def update_object_file(self, new_object_file: ObjectFile) -> None:
        self.repo.update_object_file(new_object_file)

    def delete_object_file_by_id(self, id: int) -> None:
        self.repo.delete_object_file_by_id(id)
