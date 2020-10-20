from typing import List

from mks_backend.models.inspections.inspection import Inspection
from mks_backend.repositories.inspections.inspection import InspectionRepository


class InspectionService:

    def __init__(self):
        self.repo = InspectionRepository()

    def get_all_inspections(self) -> List[Inspection]:
        return self.repo.get_all_inspections()

    def get_inspection_by_id(self, id: int) -> Inspection:
        return self.repo.get_inspection_by_id(id)

    def add_inspection(self, inspection: Inspection) -> None:
        self.repo.add_inspection(inspection)

    def update_inspection(self, new_inspection: Inspection) -> None:
        self.repo.update_inspection(new_inspection)

    def delete_inspection_by_id(self, id: int) -> None:
        self.repo.delete_inspection_by_id(id)

    def get_inspections(self, filter_params=None) -> List[Inspection]:
        if filter_params:
            params = self.switch_case(filter_params)
            return self.repo.get_filtered_inspections(params)
        else:
            return self.repo.get_all_inspections()

    def switch_case(self, filter_params: dict) -> dict:
        # TODO: rework with MKSBRYANS-227
        return filter_params

