from mks_backend.models.constructions import LocationType
from mks_backend.repositories.constructions.location_type import LocationTypeRepository


class LocationTypeService:

    def __init__(self):
        self.repo = LocationTypeRepository()

    def get_all_location_types(self) -> list:
        return self.repo.get_all_location_types()

    def get_location_type_by_id(self, id: int) -> LocationType:
        return self.repo.get_location_type_by_id(id)

    def add_location_type(self, location_type: LocationType) -> None:
        self.repo.add_location_type(location_type)

    def update_location_type(self, new_location_type: LocationType) -> None:
        self.repo.update_location_type(new_location_type)

    def delete_location_type_by_id(self, id: int) -> None:
        self.repo.delete_location_type_by_id(id)
