from .model import Coordinate
from .repository import CoordinateRepository


class CoordinateService:

    def __init__(self):
        self.repo = CoordinateRepository()

    def get_all_coordinates(self):
        return self.repo.get_all_coordinates()

    def add_coordinate(self, coordinate: Coordinate) -> None:
        self.repo.add_coordinate(coordinate)

    def update_coordinate(self, coordinate: Coordinate) -> None:
        self.repo.update_coordinate(coordinate)

    def add_or_update_coordinate(self, coordinate: Coordinate) -> None:
        if not coordinate:  # TODO: remove when MIV and IHI will be good
            return
        if coordinate.coordinates_id:
            self.update_coordinate(coordinate)
        else:
            self.add_coordinate(coordinate)
