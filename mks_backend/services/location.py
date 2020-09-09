from mks_backend.models.location import Location
from mks_backend.repositories.location import LocationRepository


class LocationService:

    @classmethod
    def add_location(cls, location: Location) -> None:
        LocationRepository.add_location(location)

    @classmethod
    def update_location(cls, location: Location) -> None:
        LocationRepository.update_location(location)