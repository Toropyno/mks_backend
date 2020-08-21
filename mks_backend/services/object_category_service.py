from mks_backend.repositories.object_categories_repository import ObjectCategoryRepository
from mks_backend.errors.db_basic_error import DBBasicError


class ObjectCategoryService:

    def __init__(self):
        self.repo = ObjectCategoryRepository()

    def get_all_object_categories(self):
        return self.repo.get_all_object_categories()

    def get_object_category_by_id(self, id):
        return self.repo.get_object_category_by_id(id)

    def add_object_category(self, object_category):
        #raise ValueError('Категория объекта строительства с таким наименованием уже существует')
        try:
            self.repo.add_object_category(object_category)
        except DBAPIError as error:
            raise DBBasicError(error)

    def delete_object_category_by_id(self, id):
        self.repo.delete_object_category_by_id(id)

    def update_object_category(self, new_object_category):
        #raise ValueError('Категория объекта строительства с таким наименованием уже существует')
        try:
            self.repo.update_object_category(new_object_category)
        except DBAPIError as error:
            raise DBBasicError(error)

