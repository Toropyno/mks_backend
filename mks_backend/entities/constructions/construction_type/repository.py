from mks_backend.errors import DBBasicError
from mks_backend.session import DBSession

from .model import ConstructionType


class ConstructionTypeRepository:

    def __init__(self):
        self._query = DBSession.query(ConstructionType)

    def get_all_construction_types(self) -> list:
        return self._query.order_by(ConstructionType.fullname).all()

    def add_construction_type(self, construction_type: ConstructionType) -> None:
        DBSession.add(construction_type)
        DBSession.commit()

    def delete_construction_type_by_id(self, id_: int) -> None:
        construction_type = self.get_construction_type_by_id(id_)
        if construction_type.constructions:
            raise DBBasicError('construction_type_limit')

        DBSession.delete(construction_type)
        DBSession.commit()

    def update_construction_type(self, new_construction_type: ConstructionType) -> None:
        if DBSession.merge(new_construction_type) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('construction_type_ad')

    def get_construction_type_by_id(self, id_: int) -> ConstructionType:
        construction_type = self._query.get(id_)
        if not construction_type:
            raise DBBasicError('construction_type_nf')
        return construction_type
