from mks_backend.models.construction import Construction
from mks_backend.serializers.utils.date_and_time import get_date_string
from mks_backend.serializers.commision import CommissionSerializer
from mks_backend.serializers.construction_category import ConstructionCategorySerializer
from mks_backend.serializers.construction_subcategory import ConstructionSubcategorySerializer
from mks_backend.serializers.coordinate import CoordinateSerializer
from mks_backend.serializers.location_type import LocationTypeSerializer
from mks_backend.serializers.military_unit import MilitaryUnitSerializer
from mks_backend.serializers.construction_company import ConstructionCompanySerializer
from mks_backend.serializers.oksm import OKSMSerializer
from mks_backend.serializers.construction_type import ConstructionTypeSerializer


class ConstructionSerializer:

    def convert_object_to_json(self, construction: Construction, object_calc=None) -> dict:
        # return with all subcategories
        category = ConstructionCategorySerializer.convert_object_to_json(
            construction.construction_category
        )

        if construction.subcategories_list:
            subcategory = ConstructionSubcategorySerializer.convert_object_to_json(
                construction.subcategories_list.subcategory
            )
        else:
            subcategory = None

        if object_calc:
            plan = object_calc.get('plan'),
            actually = object_calc.get('actually'),
            difference = object_calc.get('difference'),
            entered = object_calc.get('entered'),
            readiness = object_calc.get('readiness'),
            workers = object_calc.get('workers'),
            equipment = object_calc.get('equipment')
        else:
            plan = 0,
            actually = 0
            difference = 0
            entered = 0
            readiness = 0
            workers = 0
            equipment = 0

        return {
            'id': construction.construction_id,
            'code': construction.project_code,
            'name': construction.project_name,
            'constructionType': ConstructionTypeSerializer.convert_object_to_json(
                construction.type
            ),
            'category': category,
            'subcategory': subcategory,
            'isCritical': construction.is_critical,
            'commission': CommissionSerializer.convert_object_to_json(
                construction.commission
            ),
            'constructionCompany': ConstructionCompanySerializer.convert_object_to_json(
                construction.construction_company
            ),
            'militaryUnit': MilitaryUnitSerializer.convert_object_to_json(
                construction.military_unit
            ),
            'contractDate': get_date_string(construction.contract_date),
            'objectsAmount': construction.object_amount,
            'plannedDate': get_date_string(construction.planned_date),

            'plan': plan,
            'actually': actually,
            'difference': difference,
            'entered': entered,
            'readiness': readiness,
            'workers': workers,
            'equipment': equipment,

            'oksm': OKSMSerializer.convert_object_to_json(
                construction.oksm
            ),
            'locationType': LocationTypeSerializer.convert_object_to_json(
                construction.location_type
            ),
            'fias': {
                'subject': {
                    'id': 1,
                    'fullName': 'Название субъекта по ФИАС'
                },
                'district': {
                    'id': 11,
                    'fullName': 'Название района по ФИАС'
                },
                'city': {
                    'id': 17,
                    'fullName': 'Наименование города по ФИАС'
                },
                'locality': {
                    'id': 1,
                    'fullName': 'Наименование населенного пункта по ФИАС'
                }
            },
            'address': 'Не формализованный адрес проекта',
            'note': 'Примечание к проекту',
            'coordinate': CoordinateSerializer.convert_object_to_json(
                construction.coordinate
            ),
        }

    def convert_list_to_json(self, constructions: list) -> list:
        return list(map(self.convert_object_to_json, constructions))
