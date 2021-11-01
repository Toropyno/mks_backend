from .model import LocationType
from .repository import LocationTypeRepository


class LocationTypeService:

    def __init__(self):
        self.repo = LocationTypeRepository()

    def get_all_location_types(self) -> list:
        return self.repo.get_all_location_types()

    def get_location_type_by_id(self, id_: int) -> LocationType:
        return self.repo.get_location_type_by_id(id_)

    def add_location_type(self, location_type: LocationType) -> None:
        self.repo.add_location_type(location_type)

    def update_location_type(self, new_location_type: LocationType) -> None:
        self.repo.update_location_type(new_location_type)

    def delete_location_type_by_id(self, id_: int) -> None:
        self.repo.delete_location_type_by_id(id_)
