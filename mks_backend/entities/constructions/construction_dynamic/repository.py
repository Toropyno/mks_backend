from typing import List

from mks_backend.errors import DBBasicError
from mks_backend.session import DBSession

from .model import ConstructionDynamic


class ConstructionDynamicRepository:

    def __init__(self):
        self._query = DBSession.query(ConstructionDynamic)

    def get_construction_dynamics_by_construction_id(self, construction_id: int) -> List[ConstructionDynamic]:
        return self._query.filter(ConstructionDynamic.construction_id == construction_id).\
            order_by(ConstructionDynamic.reporting_date).all()

    def get_construction_dynamic_by_id(self, id_: int) -> ConstructionDynamic:
        return self._query.get(id_)

    def add_construction_dynamic(self, construction_dynamic: ConstructionDynamic) -> None:
        DBSession.add(construction_dynamic)
        DBSession.commit()

    def update_construction_dynamic(self, construction_dynamic: ConstructionDynamic) -> None:
        if DBSession.merge(construction_dynamic) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('construction_dynamic_ad')

    def delete_construction_dynamic(self, id_: int) -> None:
        construction_dynamic = self.get_construction_dynamic_by_id(id_)
        DBSession.delete(construction_dynamic)
        DBSession.commit()
