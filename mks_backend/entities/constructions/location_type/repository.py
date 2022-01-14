from mks_backend.errors import DBBasicError
from mks_backend.session import DBSession

from .model import LocationType


class LocationTypeRepository:

    def __init__(self):
        self._query = DBSession.query(LocationType)

    def get_all_location_types(self) -> list:
        return self._query.order_by(LocationType.fullname).all()

    def add_location_type(self, location_type: LocationType) -> None:
        DBSession.add(location_type)
        DBSession.commit()

    def delete_location_type_by_id(self, id_: int) -> None:
        self._query.filter(LocationType.location_types_id == id_).delete()
        DBSession.commit()

    def update_location_type(self, new_location_type: LocationType) -> None:
        if DBSession.merge(new_location_type) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('location_type_ad')

    def get_location_type_by_id(self, id_: int) -> LocationType:
        return self._query.get(id_)
