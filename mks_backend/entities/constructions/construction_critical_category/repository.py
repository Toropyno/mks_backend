from .model import ConstructionCriticalCategory
from mks_backend.session import DBSession

from mks_backend.errors import DBBasicError

class ConstructionCriticalCategoryRepository:

    def __init__(self):
        self._query = DBSession.query(ConstructionCriticalCategory)

    def get_construction_critical_category_by_id(self, id: int) -> ConstructionCriticalCategory:
        return self._query.get(id)

    def get_all_construction_critical_categories(self) -> list:
        return self._query.order_by(ConstructionCriticalCategory.fullname).all()

    def add_construction_critical_category(self, construction_critical_category: ConstructionCriticalCategory) -> None:
        DBSession.add(construction_critical_category)
        DBSession.commit()

    def delete_construction_critical_category_by_id(self, id: int) -> None:
        construction_critical_category = self.get_construction_critical_category_by_id(id)
        DBSession.delete(construction_critical_category)
        DBSession.commit()

    def update_construction_critical_category(self, construction_critical_category: ConstructionCriticalCategory) -> None:
        if DBSession.merge(construction_critical_category) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('construction_category_ad')
