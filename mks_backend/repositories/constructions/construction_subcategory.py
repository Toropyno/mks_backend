from mks_backend.models.constructions import ConstructionSubcategory
from mks_backend.models import DBSession

from mks_backend.errors import db_error_handler, DBBasicError


class ConstructionSubcategoryRepository:

    def __init__(self):
        self._query = DBSession.query(ConstructionSubcategory)

    def get_construction_subcategory_by_id(self, id: int) -> ConstructionSubcategory:
        return self._query.get(id)

    def get_all_construction_subcategories(self) -> list:
        return self._query.all()

    def get_many_construction_subcategories_by_id(self, ids: list) -> list:
        return self._query.filter(
            ConstructionSubcategory.construction_subcategories_id.in_(ids)
        ).all()

    @db_error_handler
    def add_construction_subcategory(self, construction_subcategory: ConstructionSubcategory):
        DBSession.add(construction_subcategory)
        DBSession.commit()

    def delete_construction_subcategory_by_id(self, id: int) -> None:
        construction_subcategory = self.get_construction_subcategory_by_id(id)
        DBSession.delete(construction_subcategory)
        DBSession.commit()

    @db_error_handler
    def update_construction_subcategory(self, construction_subcategory: ConstructionSubcategory) -> None:
        if DBSession.merge(construction_subcategory) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('construction_subcategory_ad')
