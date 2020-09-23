from mks_backend.models.coordinate import Coordinate
from mks_backend.repositories.coordinate import CoordinateRepository


class CoordinateService:

    def __init__(self):
        self.repo = CoordinateRepository()

    def get_all_locations(self):
        return self.repo.get_all_locations()

    def add_location(self, location: Coordinate) -> None:
        self.repo.add_location(location)

    def update_location(self, location: Coordinate) -> None:
        self.repo.update_location(location)

    def add_or_update_location(self, location: Coordinate) -> None:
        if not location:  # TODO: remove when MIV and IHI will be good
            return
        if location.id:
            self.update_location(location)
        else:
            self.add_location(location)
