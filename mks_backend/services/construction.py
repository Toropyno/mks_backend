from mks_backend.models.construction import Construction
from mks_backend.repositories.construction import ConstructionRepository


class ConstructionService:
    def __init__(self):
        self.repo = ConstructionRepository()

    def get_all_constructions(self) -> list:
        return self.repo.get_all_constructions()

    def get_construction_by_id(self, id: int) -> Construction:
        return self.repo.get_construction_by_id(id)

    def add_construction(self, construction: Construction) -> None:
        self.repo.add_construction(construction)

    def update_construction(self, new_construction: Construction) -> None:
        self.repo.update_construction(new_construction)

    def delete_construction_by_id(self, id: int) -> None:
        self.repo.delete_construction(id)

    def filter_constructions(self, params: dict) -> list:
        params = self.get_params_from_schema(params)
        return self.repo.filter_constructions(params)

    def get_params_from_schema(self, params_deserilized: dict) -> dict:
        case_switcher = {
            'code': 'project_code',
            'name': 'project_name',
            'category': 'constructions_categories_id',
            'subcategory': 'subcategories_list_id',
            'isCritical': 'is_critical',
            'commission': 'commission_id',
            'militaryUnit': 'idMU',
            'objectsAmount': 'object_amount',
            'contractDateStart': 'contract_date_start',
            'contractDateEnd': 'contract_date_end',
            'plannedDateStart': 'planned_date_start',
            'plannedDateEnd': 'planned_date_end',
        }

        params = dict()
        for key, value in params_deserilized.items():
            if key in case_switcher and value is not None:
                params[case_switcher[key]] = params_deserilized[key]

        return params
