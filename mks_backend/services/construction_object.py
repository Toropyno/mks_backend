from mks_backend.models.construction_object import ConstructionObject
from mks_backend.repositories.construction_object import ConstructionObjectRepository
from mks_backend.services.location import LocationService


class ConstructionObjectService:

    def __init__(self):
        self.repo = ConstructionObjectRepository()
        self.location_service = LocationService()

    def get_all_construction_objects_by_construction_id(self, construction_id: int) -> list:
        return self.repo.get_all_construction_objects_by_construction_id(construction_id)

    def get_construction_object_by_id(self, id: int) -> ConstructionObject:
        return self.repo.get_construction_object_by_id(id)

    def add_construction_object(self, construction_object: ConstructionObject) -> None:
        self.repo.add_construction_object(construction_object)

    def delete_construction_object_by_id(self, id: int) -> None:
        self.repo.delete_construction_object_by_id(id)

    def update_construction_object(self, new_construction_object: ConstructionObject) -> None:
        self.location_service.add_or_update_location(new_construction_object.location)
        self.repo.update_construction_object(new_construction_object)
