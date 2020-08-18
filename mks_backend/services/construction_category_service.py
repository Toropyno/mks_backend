from mks_backend.repositories.construction_categories_repository import ConstructionCategoryRepository
from mks_backend.models.construction_categories import ConstructionCategories


class ConstructionCategoriesService:

    def __init__(self):
        self.repo = ConstructionCategoryRepository()

    def get_construction_category_by_id(self, id):
        return self.repo.get_construction_category_by_id(id)

    def add_construction_category(self, construction_categories):
        return self.repo.add_construction_category(construction_categories)

    def delete_construction_category_by_id(self, id):
        self.repo.delete_construction_category_by_id(id)

    def update_construction_category(self, construction_category):
        self.repo.update_construction_category(construction_category)

    def get_all_construction_categories(self):
        return self.repo.get_all_construction_categories()

    def convert_schema_to_object(self, schema):
        construction_categories = ConstructionCategories()

        construction_categories.construction_categories_id = schema.get('id')
        construction_categories.fullname = schema.get('fullName')

        return construction_categories
