from typing import List

from .model import Inspection
from .repository import InspectionRepository


class InspectionService:

    def __init__(self):
        self.repo = InspectionRepository()

    def get_all_inspections(self) -> List[Inspection]:
        return self.repo.get_all_inspections()

    def get_inspection_by_id(self, id_: int) -> Inspection:
        return self.repo.get_inspection_by_id(id_)

    def add_inspection(self, inspection: Inspection) -> None:
        self.repo.add_inspection(inspection)

    def update_inspection(self, new_inspection: Inspection) -> None:
        self.repo.update_inspection(new_inspection)

    def delete_inspection_by_id(self, id_: int) -> None:
        self.repo.delete_inspection_by_id(id_)

    def get_inspections(self, filter_params=None) -> List[Inspection]:
        if filter_params:
            params = self.switch_case(filter_params)
            return self.repo.get_filtered_inspections(params)
        else:
            return self.repo.get_all_inspections()

    def switch_case(self, filter_params: dict) -> dict:
        case_switcher = {
            'dateStart': 'date_start',
            'dateEnd': 'date_end',
            'name': 'name',
            'inspector': 'inspector',
            'haveFile': 'have_file',
            'haveInspectedObjects': 'have_inspected_objects',
            'constructionCode': 'construction_code',
            'isCritical': 'is_critical',
            'fiasSubject': 'fias_subject'
        }

        params = dict()
        for key in filter_params:
            params[case_switcher[key]] = filter_params[key]

        return params
