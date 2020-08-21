from mks_backend.errors.db_basic_error import db_error_handler
from mks_backend.repositories.subcategories_list_repository import SubcategoriesListRepository


class SubcategoriesListService:

    def __init__(self):
        self.repo = SubcategoriesListRepository()

    def get_subcategories_list_by_id(self, id):
        return self.repo.get_subcategories_list_by_id(id)

    @db_error_handler
    def add_subcategories_list(self, subcategories_list):
        return self.repo.add_subcategories_list(subcategories_list)

    def delete_subcategories_list_by_id(self, id):
        self.repo.delete_subcategories_list_by_id(id)

    def get_all_subcategories_lists(self):
        return self.repo.get_all_subcategories_lists()

    def get_uniq_error_message(self, uniq_error):
        uniq_error = uniq_error.args[0]
        u = ""
        if "subcategories" in uniq_error:
            u += " construction_subcategories_id"
        if "_categories_id" in uniq_error:
            u += " construction_categories_id"
        return u
