from mks_backend.models.location import Location
from mks_backend.repositories.location import LocationRepository


class LocationService:

    def __init__(self):
        self.repo = LocationRepository()

    def get_all_locations(self):
        return self.repo.get_all_locations()

    def add_location(self, location: Location) -> None:
        self.repo.add_location(location)

    def update_location(self, location: Location) -> None:
        self.repo.update_location(location)

    def add_or_update_location(self, location: Location) -> None:
        if location.id:
            self.update_location(location)
        else:
            self.add_location(location)
