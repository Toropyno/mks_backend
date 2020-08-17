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

    def get_object(self, json_body):
        subcategories_list = SubcategoriesList()
        if 'subcategoriesListId' in json_body:
            subcategories_list.subcategories_list_id = json_body['subcategoriesListId']
        subcategories_list.construction_categories_id = json_body['constructionCategoriesId']
        subcategories_list.construction_subcategories_id = json_body['constructionSubcategoriesId']
        return subcategories_list