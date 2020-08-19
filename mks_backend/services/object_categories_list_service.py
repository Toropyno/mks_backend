from mks_backend.models.object_categories_list import ObjectCategoriesList
from mks_backend.repositories.object_categories_lists_repository import ObjectCategoriesListRepository


class ObjectCategoriesListService:

    def __init__(self):
        self.repo = ObjectCategoriesListRepository()

    def get_all_object_categories_lists(self):
        return self.repo.get_all_object_categories_lists()

    def get_object_categories_list_by_id(self, id):
        return self.repo.get_object_categories_list_by_id(id)

    def add_object_categories_list(self, object_categories_list):
        if self.repo.get_object_categories_list_by_zone_id(object_categories_list.zones_id):
            raise ValueError('Перечень категорий объектов с указанной зоной военного городка уже существует')
        if self.repo.get_object_categories_list_by_object_categories_id(object_categories_list.object_categories_id):
            raise ValueError('Перечень категорий объектов с указанной категорией объекта строительства уже существует')
        self.repo.add_object_categories_list(object_categories_list)

    def delete_object_categories_list_by_id(self, id):
        self.repo.delete_object_categories_list_by_id(id)

    def update_object_categories_list(self, new_object_categories_list):
        old_object_categories_list = self.repo.get_object_categories_list_by_id(new_object_categories_list.object_categories_list_id)
        if old_object_categories_list.zones_id != new_object_categories_list.zones_id:
            if self.repo.get_object_categories_list_by_zone_id(new_object_categories_list.zones_id):
                raise ValueError('Перечень категорий объектов с указанной зоной военного городка уже существует')
        if old_object_categories_list. object_categories_id != new_object_categories_list.object_categories_id:
            if self.repo.get_object_categories_list_by_object_categories_id(
                    new_object_categories_list.object_categories_id):
                raise ValueError(
                    'Перечень категорий объектов с указанной категорией объекта строительства уже существует')
        self.repo.update_object_categories_list(new_object_categories_list)