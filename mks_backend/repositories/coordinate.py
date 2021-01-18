from mks_backend.models.coordinate import Coordinate
from mks_backend.session import DBSession


class CoordinateRepository:

    def __init__(self):
        self._query = DBSession.query(Coordinate)

    def get_all_coordinates(self) -> list:
        return self._query.all()

    def add_coordinate(self, coordinate: Coordinate) -> None:
        DBSession.add(coordinate)

    def update_coordinate(self, coordinate: Coordinate) -> None:
        self._query.filter_by(coordinates_id=coordinate.coordinates_id).update(
            {
                'longitude': coordinate.longitude,
                'latitude': coordinate.latitude,
                'zoom': coordinate.zoom
            }
        )
