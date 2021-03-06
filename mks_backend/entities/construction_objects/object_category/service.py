from .model import ObjectCategory
from .repository import ObjectCategoryRepository


class ObjectCategoryService:

    def __init__(self):
        self.repo = ObjectCategoryRepository()

    def get_all_object_categories(self) -> list:
        return self.repo.get_all_object_categories()

    def get_many_object_categories_by_id(self, ids: list) -> list:
        return self.repo.get_many_object_categories_by_id(ids)

    def get_object_category_by_id(self, id_: int) -> ObjectCategory:
        return self.repo.get_object_category_by_id(id_)

    def add_object_category(self, object_category: ObjectCategory) -> None:
        self.repo.add_object_category(object_category)

    def delete_object_category_by_id(self, id_: int) -> None:
        self.repo.delete_object_category_by_id(id_)

    def update_object_category(self, new_object_category: ObjectCategory) -> None:
        self.repo.update_object_category(new_object_category)
