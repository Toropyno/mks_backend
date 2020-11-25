from mks_backend.models.constructions import LocationType
from mks_backend.models import DBSession

from mks_backend.errors import db_error_handler, DBBasicError


class LocationTypeRepository:

    def __init__(self):
        self._query = DBSession.query(LocationType)

    def get_all_location_types(self) -> list:
        return self._query.order_by(LocationType.fullname).all()

    @db_error_handler
    def add_location_type(self, location_type: LocationType) -> None:
        DBSession.add(location_type)
        DBSession.commit()

    def delete_location_type_by_id(self, id: int) -> None:
        self._query.filter(LocationType.location_types_id == id).delete()
        DBSession.commit()

    @db_error_handler
    def update_location_type(self, new_location_type: LocationType) -> None:
        if DBSession.merge(new_location_type) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('location_type_ad')

    def get_location_type_by_id(self, id: int) -> LocationType:
        return self._query.get(id)
