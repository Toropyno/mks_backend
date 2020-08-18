from mks_backend.repositories.subcategories_list_repository import SubcategoriesListRepository
from mks_backend.models.subcategories_list import SubcategoriesList


class SubcategoriesListService:

    def __init__(self):
        self.repo = SubcategoriesListRepository()

    def get_subcategories_list_by_id(self, id):
        return self.repo.get_subcategories_list_by_id(id)

    def add_subcategories_list(self, subcategories_list):
        return self.repo.add_subcategories_list(subcategories_list)

    def delete_subcategories_list_by_id(self, id):
        self.repo.delete_subcategories_list_by_id(id)

    def get_all_subcategories_lists(self):
        return self.repo.get_all_subcategories_lists()

    def convert_schema_to_object(self, schema):
        subcategories_lists = SubcategoriesList()

        subcategories_lists.construction_categories_id = schema.get('constructionCategoriesId')
        subcategories_lists.construction_subcategories_id = schema.get('constructionSubcategoriesId')

        return subcategories_lists
