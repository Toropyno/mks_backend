from mks_backend.models.location_type import LocationType
from mks_backend.repositories import DBSession

from mks_backend.errors.db_basic_error import db_error_handler


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
        old_location_type = self._query.filter_by(location_types_id=new_location_type.location_types_id)
        old_location_type.update(
            {
                'fullname': new_location_type.fullname,
            }
        )

        DBSession.commit()

    def get_location_type_by_id(self, id: int) -> LocationType:
        return self._query.get(id)
