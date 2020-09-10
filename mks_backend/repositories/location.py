from mks_backend.models.location import Location
from mks_backend.repositories import DBSession


class LocationRepository:

    def get_all_locations(self) -> list:
        return DBSession.query(Location).all()

    def add_location(self, location: Location) -> None:
        DBSession.add(location)

    def update_location(self, location: Location) -> None:
        DBSession.query(Location).filter_by(id=location.id).update(
            {
                'longitude': location.longitude,
                'latitude': location.latitude,
                'zoom': location.zoom
            }
        )
