from mks_backend.models.object_categories import ObjectCategories
from mks_backend.repositories.object_categories_repository import ObjectCategoryRepository


class ObjectCategoryService:

    def __init__(self):
        self.repo = ObjectCategoryRepository()

    def get_all_object_categories(self):
        return self.repo.get_all_object_categories()

    def get_object_category_by_id(self, id):
        return self.repo.get_object_category_by_id(id)

    def add_object_category(self, object_category):
        if self.repo.get_object_category_by_fullname(object_category.fullname):
            raise ValueError('Категория объекта строительства с таким наименованием уже существует.')
        self.repo.add_object_category(object_category)

    def delete_object_category_by_id(self, id):
        self.repo.delete_object_category_by_id(id)

    def update_object_category(self, new_object_category):
        self.repo.update_object_category(new_object_category)

    def get_object(self, json_body):
        object_category = ObjectCategories()
        if 'id' in json_body:
            object_category.object_categories_id = json_body['id']

        object_category.fullname = json_body['fullName']
        object_category.note = json_body['note']
        return object_category
