from mks_backend.repositories.object_categories_repository import ObjectCategoryRepository


class ObjectCategoryService:

    def _init_(self):
        self.repo = ObjectCategoryRepository()

    def get_all_object_categories(self):
        return self.repo.get_all_object_categories()

    def get_object_category_by_id(self, id):
        return self.repo.get_object_category_by_id(id)

    def add_object_category(self, object_category):
        self.repo.add_object_category(object_category)

    def delete_object_category_by_id(self, id):
        self.repo.delete_object_category_by_id(id)

    def update_object_category(self, new_object_category):
        self.repo.update_object_category(new_object_category)
