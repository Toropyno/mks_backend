from mks_backend.models.realty_type import RealtyType
from mks_backend.models import DBSession

from mks_backend.errors.db_basic_error import db_error_handler


class RealtyTypeRepository:

    def __init__(self):
        self._query = DBSession.query(RealtyType)

    def get_all_realty_types(self) -> list:
        return self._query.order_by(RealtyType.fullname).all()

    @db_error_handler
    def add_realty_type(self, realty_type: RealtyType) -> None:
        DBSession.add(realty_type)
        DBSession.commit()

    def delete_realty_type_by_id(self, id: int) -> None:
        self._query.filter(RealtyType.realty_types_id == id).delete()
        DBSession.commit()

    @db_error_handler
    def update_realty_type(self, new_realty_type: RealtyType) -> None:
        DBSession.merge(new_realty_type)
        DBSession.commit()

    def get_realty_type_by_id(self, id: int) -> RealtyType:
        return self._query.get(id)
