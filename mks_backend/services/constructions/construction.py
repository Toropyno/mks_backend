from uuid import uuid4

from mks_backend.models.constructions import Construction
from mks_backend.repositories.constructions.construction import ConstructionRepository
from mks_backend.services.construction_objects.construction_object import ConstructionObjectService
from mks_backend.services.coordinate import CoordinateService
from mks_backend.services.constructions.subcategory_list import SubcategoryListService

from mks_backend.models.fias import FIAS


class ConstructionService:

    def __init__(self):
        self.repo = ConstructionRepository()
        self.subcategory_list_service = SubcategoryListService()
        self.coordinate_service = CoordinateService()
        self.object_service = ConstructionObjectService()

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
        construction.military_district_id = schema.get('militaryDistrict')
        construction.object_amount = schema.get('objectsAmount')
        construction.coordinates_id = schema.get('coordinateId')
        construction.construction_types_id = schema.get('constructionType')
        construction.location_types_id = schema.get('locationType')
        construction.construction_companies_id = schema.get('constructionCompany')
        construction.oksm_id = schema.get('oksm')
        construction.address_full = schema.get('address')
        construction.note = schema.get('note')
        construction.organizations_id = schema.get('organization')
        construction.department = schema.get('department')
        construction.officer = schema.get('officer')
        construction.technical_spec = schema.get('technicalSpec')
        construction.price_calc = schema.get('priceCalc')
        construction.deletion_mark = schema.get('deletionMark')

        category_id = schema.get('category')
        subcategory_id = schema.get('subcategory')
        construction.construction_categories_id = category_id
        if subcategory_id:
            subcategories_list = self.subcategory_list_service.get_subcategories_list_by_relations(
                category_id, subcategory_id
            )
            construction.subcategories_list_id = subcategories_list.subcategories_list_id

        fias = schema.get('fias')
        if fias:
            # some cool stuff for FIAS
            pass
        else:
            # TODO: remove when FIAS will be ok
            region = schema.get('region')
            area = schema.get('area')
            city = schema.get('city')
            settlement = schema.get('settlement')
            street = schema.get('street')

            construction.fias = FIAS(aoid=uuid4(), region=region, area=area,
                                     city=city, settlement=settlement, street=street)

        return construction

    def filter_constructions(self, params: dict) -> list:
        params = self.get_params_from_schema(params)

        if 'subcategories_list_id' in params:
            # frontend doesn't know about many-to-many and send category_id and subcategory_id
            params['subcategories_list_id'] = self.subcategory_list_service.get_subcategories_list_by_relations(
                params['constructions_categories_id'], params['subcategories_list_id']
            ).subcategories_list_id

        return self.repo.filter_constructions(params)

    def get_params_from_schema(self, params_deserialized: dict) -> dict:
        case_switcher = {
            'code': 'project_code',
            'name': 'project_name',
            'category': 'constructions_categories_id',
            'subcategory': 'subcategories_list_id',
            'isCritical': 'is_critical',
            'commission': 'commission_id',
            'militaryUnit': 'idMU',
            'objectsAmount': 'object_amount',
            'plannedDateStart': 'planned_date_start',
            'plannedDateEnd': 'planned_date_end',
            'constructionType': 'construction_types_id',
            'company': 'construction_companies_id',
            'locationType': 'location_types_id',
            'oksm': 'oksm_id',
            'address': 'address',

            'organization': 'organization',
            'readiness': 'readiness',
            'deletionMark': 'deletion_mark',
            'militaryDistrict': 'military_district',

            'region': 'region',
            'area': 'area',
            'city': 'city',
            'settlement': 'settlement',
        }

        params = dict()
        for key, value in params_deserialized.items():
            if key in case_switcher and value is not None:
                params[case_switcher[key]] = params_deserialized[key]

        return params
