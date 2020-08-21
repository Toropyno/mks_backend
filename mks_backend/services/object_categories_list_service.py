from mks_backend.repositories.object_categories_lists_repository import ObjectCategoriesListRepository
from mks_backend.errors.db_basic_error import DBBasicError


class ObjectCategoriesListService:

    def __init__(self):
        self.repo = ObjectCategoriesListRepository()

    def get_all_object_categories_lists(self):
        return self.repo.get_all_object_categories_lists()

    def get_object_categories_list_by_id(self, id):
        return self.repo.get_object_categories_list_by_id(id)

    def add_object_categories_list(self, object_categories_list):
        #raise ValueError('Перечень категорий объектов с указанной зоной военного городка уже существует')
        #raise ValueError('Перечень категорий объектов с указанной категорией объекта строительства уже существует')
        try:
            self.repo.add_object_categories_list(object_categories_list)
        except DBAPIError as error:
            raise DBBasicError(error)

    def delete_object_categories_list_by_id(self, id):
        self.repo.delete_object_categories_list_by_id(id)

    def update_object_categories_list(self, new_object_categories_list):
        #raise ValueError('Перечень категорий объектов с указанной зоной военного городка уже существует')
        #raise ValueError('Перечень категорий объектов с указанной категорией объекта строительства уже существует')
        try:
            self.repo.update_object_categories_list(new_object_categories_list)
        except DBAPIError as error:
            raise DBBasicError(error)