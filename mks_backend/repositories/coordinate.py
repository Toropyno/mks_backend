from mks_backend.models.coordinate import Coordinate
from mks_backend.repositories import DBSession


class CoordinateRepository:

    def get_all_locations(self) -> list:
        return DBSession.query(Coordinate).all()

    def add_location(self, location: Coordinate) -> None:
        DBSession.add(location)

    def update_location(self, location: Coordinate) -> None:
        DBSession.query(Coordinate).filter_by(id=location.id).update(
            {
                'longitude': location.longitude,
                'latitude': location.latitude,
                'zoom': location.zoom
            }
        )
