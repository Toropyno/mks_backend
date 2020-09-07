from mks_backend.models.object_category import ObjectCategory
from mks_backend.repositories.object_category import ObjectCategoryRepository


class ObjectCategoryService:

    def __init__(self):
        self.repo = ObjectCategoryRepository()

    def get_all_object_categories(self) -> list:
        return self.repo.get_all_object_categories()

    def get_object_category_by_id(self, id: int) -> ObjectCategory:
        return self.repo.get_object_category_by_id(id)

    def add_object_category(self, object_category: ObjectCategory) -> None:
        self.repo.add_object_category(object_category)

    def delete_object_category_by_id(self, id: int) -> None:
        self.repo.delete_object_category_by_id(id)

    def update_object_category(self, new_object_category: ObjectCategory) -> None:
        self.repo.update_object_category(new_object_category)
