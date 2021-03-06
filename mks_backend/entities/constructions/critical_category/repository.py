from mks_backend.errors import DBBasicError
from mks_backend.session import DBSession

from .model import CriticalCategory


class CriticalCategoryRepository:

    def __init__(self):
        self._query = DBSession.query(CriticalCategory)

    def get_critical_category_by_id(self, id_: int) -> CriticalCategory:
        critical_category = self._query.get(id_)
        if not critical_category:
            raise DBBasicError('critical_category_nf')
        return critical_category

    def get_all_critical_category(self) -> list:
        return self._query.order_by(CriticalCategory.fullname).all()

    def add_critical_category(self, critical_category: CriticalCategory) -> None:
        DBSession.add(critical_category)
        DBSession.commit()

    def delete_critical_category_by_id(self, id_: int) -> None:
        critical_category = self.get_critical_category_by_id(id_)
        DBSession.delete(critical_category)
        DBSession.commit()

    def update_critical_category(self, critical_category: CriticalCategory) -> None:
        if DBSession.merge(critical_category) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('critical_category_ad')
