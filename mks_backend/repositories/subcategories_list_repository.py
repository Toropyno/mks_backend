from mks_backend.models.subcategories_list import SubcategoriesList
from mks_backend.repositories import DBSession


class SubcategoriesListRepository:

    @classmethod
    def get_subcategories_list_by_id(cls, id):
        return DBSession.query(SubcategoriesList).get(id)

    def get_all_subcategories_lists(self):
        return DBSession.query(SubcategoriesList).all()

    def add_subcategories_list(self, subcategories_list):
        DBSession.add(subcategories_list)
        DBSession.commit()

    def delete_subcategories_list_by_id(self, id):
        subcategories_list = self.get_subcategories_list_by_id(id)
        DBSession.delete(subcategories_list)
        DBSession.commit()
