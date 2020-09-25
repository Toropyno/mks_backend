from mks_backend.models.coordinate import Coordinate
from mks_backend.repositories import DBSession


class CoordinateRepository:

    def get_all_coordinates(self) -> list:
        return DBSession.query(Coordinate).all()

    def add_coordinate(self, coordinate: Coordinate) -> None:
        DBSession.add(coordinate)

    def update_coordinate(self, coordinate: Coordinate) -> None:
        DBSession.query(Coordinate).filter_by(coordinates_id=coordinate.coordinates_id).update(
            {
                'longitude': coordinate.longitude,
                'latitude': coordinate.latitude,
                'zoom': coordinate.zoom
            }
        )
