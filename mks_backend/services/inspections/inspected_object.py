from typing import List, Tuple

from mks_backend.services.inspections.inspection import InspectionService
from mks_backend.repositories.inspections.inspected_object import InspectedObjectRepository
from mks_backend.models.constructions import Construction
from mks_backend.models.inspections.inspected_object import InspectedObject


class InspectedObjectService:

    def __init__(self):
        self.inspection_service = InspectionService()
        self.repo = InspectedObjectRepository()

    def get_inspected_objects_by_inspection(self, inspection_id: int) -> List[Construction]:
        return self.inspection_service.get_inspection_by_id(inspection_id).constructions

    def delete_inspected_object(self, inspection_id: int, construction_id: int) -> None:
        self.repo.delete_inspected_object(inspection_id, construction_id)

    def add_inspected_objects(self, inspected_objects: Tuple[InspectedObject]):
        self.repo.add_inspected_objects(inspected_objects)
