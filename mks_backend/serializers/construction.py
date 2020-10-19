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

    def to_json(self, construction: Construction) -> dict:
        if construction.subcategories_list:
            subcategory = ConstructionSubcategorySerializer.convert_object_to_json(
                construction.subcategories_list.subcategory
            )
        else:
            subcategory = None

        return {
            'id': construction.construction_id,
            'code': construction.project_code,
            'name': construction.project_name,
            'constructionType': ConstructionTypeSerializer.convert_object_to_json(
                construction.type
            ),
            'category': ConstructionCategorySerializer.to_short_json(
                construction.construction_category
            ),
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
            'address': 'Неформализованный адрес проекта',
            'note': 'Примечание к проекту',
            'coordinate': CoordinateSerializer.convert_object_to_json(
                construction.coordinate
            ),

            # --------- calculated_fields --------- #
            'plan': construction.plan,
            'actually': construction.actually,
            'difference': construction.difference,
            'enteredAdditionally': construction.entered_additionally,
            'readiness': format(construction.readiness, '.3f'),
            'workers': construction.workers,
            'equipment': construction.equipment,
        }

    def convert_list_to_json(self, constructions: list) -> list:
        return list(map(self.to_json, constructions))
