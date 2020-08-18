from mks_backend.repositories.construction_subcategories_repository import ConstructionSubcategoryRepository
from mks_backend.models.construction_subcategories import ConstructionSubcategories


class ConstructionSubcategoriesService:

    def __init__(self):
        self.repo = ConstructionSubcategoryRepository()

    def get_all_construction_subcategories(self):
        return self.repo.get_all_construction_subcategories()

    def get_construction_subcategory_by_id(self, id):
        return self.repo.get_construction_subcategory_by_id(id)

    def add_construction_subcategory(self, construction_subcategory):
        self.repo.add_construction_subcategory(construction_subcategory)

    def delete_construction_subcategory_by_id(self, id):
        self.repo.delete_construction_subcategory_by_id(id)

    def update_construction_subcategory(self, construction_subcategory):
        self.repo.update_construction_subcategory(construction_subcategory)

    def convert_schema_to_object(self, schema):
        construction_subcategories = ConstructionSubcategories()

        construction_subcategories.fullname = schema.get('fullName')

        return construction_subcategories
