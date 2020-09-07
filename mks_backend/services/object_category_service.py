from mks_backend.models.object_categories import ObjectCategories
from mks_backend.repositories.object_categories_repository import ObjectCategoryRepository


class ObjectCategoryService:

    def __init__(self):
        self.repo = ObjectCategoryRepository()

    def get_all_object_categories(self) -> list:
        return self.repo.get_all_object_categories()

    def get_object_category_by_id(self, id: int) -> ObjectCategories:
        return self.repo.get_object_category_by_id(id)

    def add_object_category(self, object_category: ObjectCategories) -> None:
        self.repo.add_object_category(object_category)

    def delete_object_category_by_id(self, id: int) -> None:
        self.repo.delete_object_category_by_id(id)

    def update_object_category(self, new_object_category: ObjectCategories) -> None:
        self.repo.update_object_category(new_object_category)
