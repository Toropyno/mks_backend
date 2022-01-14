from mks_backend.errors import DBBasicError
from mks_backend.session import DBSession

from .model import ConstructionCategory


class ConstructionCategoryRepository:

    def __init__(self):
        self._query = DBSession.query(ConstructionCategory)

    def get_construction_category_by_id(self, id_: int) -> ConstructionCategory:
        return self._query.get(id_)

    def get_all_construction_categories(self) -> list:
        return self._query.order_by(ConstructionCategory.fullname).all()

    def add_construction_category(self, construction_category: ConstructionCategory) -> None:
        DBSession.add(construction_category)
        DBSession.commit()

    def delete_construction_category_by_id(self, id_: int) -> None:
        construction_category = self.get_construction_category_by_id(id_)
        DBSession.delete(construction_category)
        DBSession.commit()

    def update_construction_category(self, construction_category: ConstructionCategory) -> None:
        if DBSession.merge(construction_category) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('construction_category_ad')
