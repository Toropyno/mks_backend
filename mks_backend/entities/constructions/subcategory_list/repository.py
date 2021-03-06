from mks_backend.session import DBSession

from .model import SubcategoryList


class SubcategoryListRepository:

    def __init__(self):
        self._query = DBSession.query(SubcategoryList)

    def get_subcategories_list_by_id(self, id_: int) -> SubcategoryList:
        return self._query.get(id_)

    def get_all_subcategories_lists(self) -> list:
        return self._query.all()

    def add_subcategories_list(self, subcategories_list: SubcategoryList) -> None:
        DBSession.add(subcategories_list)
        DBSession.commit()

    def delete_subcategories_list_by_id(self, id_: int) -> None:
        self._query.filter(SubcategoryList.subcategories_list_id == id_).delete()
        DBSession.commit()

    def get_subcategories_list_by_relations(self, category_id: int, subcategory_id: int) -> SubcategoryList:
        return self._query.filter(
            SubcategoryList.construction_categories_id == category_id,
            SubcategoryList.construction_subcategories_id == subcategory_id
        ).first()
