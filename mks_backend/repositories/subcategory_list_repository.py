from mks_backend.errors.db_basic_error import db_error_handler
from mks_backend.models.subcategory_list import SubcategoryList
from mks_backend.repositories import DBSession


class SubcategoryListRepository:

    def get_subcategories_list_by_id(self, id: int) -> SubcategoryList:
        return DBSession.query(SubcategoryList).get(id)

    def get_all_subcategories_lists(self) -> list:
        return DBSession.query(SubcategoryList).all()

    @db_error_handler
    def add_subcategories_list(self, subcategories_list: SubcategoryList) -> None:
        DBSession.add(subcategories_list)
        DBSession.commit()

    def delete_subcategories_list_by_id(self, id: int) -> None:
        subcategories_list = self.get_subcategories_list_by_id(id)
        DBSession.delete(subcategories_list)
        DBSession.commit()
