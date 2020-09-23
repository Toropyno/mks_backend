from mks_backend.models.construction import Construction
from mks_backend.repositories.construction import ConstructionRepository
from mks_backend.services.coordinate import CoordinateService
from mks_backend.services.subcategory_list import SubcategoryListService


class ConstructionService:

    def __init__(self):
        self.repo = ConstructionRepository()
        self.subcategory_list_service = SubcategoryListService()
        self.coordinate_service = CoordinateService()

    def get_all_constructions(self) -> list:
        return self.repo.get_all_constructions()

    def get_construction_by_id(self, id: int) -> Construction:
        return self.repo.get_construction_by_id(id)

    def add_construction(self, construction: Construction) -> None:
        self.repo.add_construction(construction)

    def update_construction(self, new_construction: Construction) -> None:
        self.coordinate_service.add_or_update_coordinate(new_construction.coordinate)
        self.repo.update_construction(new_construction)

    def delete_construction_by_id(self, id: int) -> None:
        self.repo.delete_construction(id)

    def convert_schema_to_object(self, schema: dict) -> Construction:
        construction = Construction()

        construction.construction_id = schema.get('id')
        construction.project_code = schema.get('code')
        construction.project_name = schema.get('name')
        construction.is_critical = schema.get('isCritical')
        construction.commission_id = schema.get('commission')
        construction.idMU = schema.get('militaryUnit')
        construction.contract_date = schema.get('contractDate')
        construction.planned_date = schema.get('plannedDate')
        construction.object_amount = schema.get('objectsAmount')
        construction.coordinates_id = schema.get('coordinateId')
        construction.construction_types_id = 1  # schema.get('constructionType')
        construction.location_types_id = 1  # schema.get('locationType')
        construction.construction_companies_id = 1  # schema.get('constructionCompany')
        construction.oksm_id = 1  # schema.get('oksm')
        construction.address = 'Адрес проекта'  # schema.get('address')
        construction.note = 'Примечание к проекту'  # schema.get('note')

        category_id = schema.get('category')
        construction.construction_categories_id = category_id

        subcategory_id = schema.get('subcategory')
        if subcategory_id:
            subcategories_list = self.subcategory_list_service.get_subcategories_list_by_relations(
                category_id, subcategory_id
            )
            construction.subcategories_list_id = subcategories_list.subcategories_list_id

        fias = schema.get('fias')
        if fias:
            # some cool stuff for FIAS
            construction.id_fias = 1

        return construction

    def filter_constructions(self, params: dict) -> list:
        params = self.get_params_from_schema(params)

        if 'subcategories_list_id' in params:
            # frontend doesn't know about many-to-many and send category_id and subcategory_id
            params['subcategories_list_id'] = self.subcategory_list_service.get_subcategories_list_by_relations(
                params['constructions_categories_id'], params['subcategories_list_id']
            ).subcategories_list_id

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
