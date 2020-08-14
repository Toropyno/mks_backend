from mks_backend.repositories.construction_subcategories_repository import ConstructionSubcategoryRepository
from mks_backend.models.construction_categories import ConstructionCategories


class ConstructionSubcategoriesService:

    def __init__(self):
        self.repo = ConstructionSubcategoryRepository()

    def get_all_construction_subcategories(self):
        return self.repo.get_all_construction_subcategories()

    def get_construction_subcategory_by_id(self, id):
        return self.repo.get_construction_subcategory_by_id(id)

    def get_object(self, json_body):
        construction_subcategory = ConstructionCategories()
        construction_subcategory.construction_categories_id = json_body['constructionCategoryId']
        return construction_subcategory

    def add_construction_subcategory(self, construction_subcategory):
        self.repo.add_construction_subcategory(construction_subcategory)

    def delete_construction_subcategory_by_id(self, id):
        self.repo.delete_construction_subcategory_by_id(id)

    def update_construction_subcategory(self, construction_subcategory):
        self.repo.update_construction_subcategory(construction_subcategory)