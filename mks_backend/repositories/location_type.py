from mks_backend.models.location_type import LocationType
from mks_backend.repositories import DBSession


class LocationTypeRepository:

    def __init__(self):
        self._query = DBSession.query(LocationType)

    def get_all_location_types(self) -> list:
        return self._query.all()

    def add_location_type(self, location_type: LocationType) -> None:
        DBSession.add(location_type)
        DBSession.commit()

    def delete_location_type_by_id(self, id: int) -> None:
        self._query.filter(LocationType.location_types_id == id).delete()
        DBSession.commit()

    def update_location_type(self, location_type: LocationType) -> None:
        self._query.filter_by(location_types_id=location_type.location_types_id).update(
            {
                'fullname': location_type.fullname,
            }
        )

        DBSession.commit()

    def get_location_type_by_id(self, id: int) -> LocationType:
        return self._query.get(id)
