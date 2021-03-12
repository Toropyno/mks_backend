from mks_backend.models.construction_objects.realty_type import RealtyType
from mks_backend.session import DBSession

from mks_backend.errors import DBBasicError


class RealtyTypeRepository:

    def __init__(self):
        self._query = DBSession.query(RealtyType)

    def get_all_realty_types(self) -> list:
        return self._query.order_by(RealtyType.fullname).all()

    def add_realty_type(self, realty_type: RealtyType) -> None:
        DBSession.add(realty_type)
        DBSession.commit()

    def delete_realty_type_by_id(self, id: int) -> None:
        self._query.filter(RealtyType.realty_types_id == id).delete()
        DBSession.commit()

    def update_realty_type(self, new_realty_type: RealtyType) -> None:
        if DBSession.merge(new_realty_type) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('realty_type_ad')

    def get_realty_type_by_id(self, id: int) -> RealtyType:
        return self._query.get(id)
