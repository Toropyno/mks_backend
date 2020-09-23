from mks_backend.models.construction import Construction
from mks_backend.serializers._date_utils import get_date_string
from mks_backend.serializers.commision import CommissionSerializer
from mks_backend.serializers.construction_category import ConstructionCategorySerializer
from mks_backend.serializers.construction_subcategory import ConstructionSubcategorySerializer
from mks_backend.serializers.location import LocationSerializer
from mks_backend.serializers.location_type import LocationTypeSerializer
from mks_backend.serializers.military_unit import MilitaryUnitSerializer
from mks_backend.serializers.construction_company import ConstructionCompanySerializer
from mks_backend.serializers.oksm import OKSMSerializer
from mks_backend.serializers.construction_type import ConstructionTypeSerializer


class ConstructionSerializer:

    def convert_object_to_json(self, construction: Construction) -> dict:
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

        return {
            'id': construction.construction_id,
            'code': construction.project_code,
            'name': construction.project_name,
            'category': category,
            'subcategory': subcategory,
            'isCritical': construction.is_critical,
            'commission': CommissionSerializer.convert_object_to_json(
                construction.commission
            ),
            'militaryUnit': MilitaryUnitSerializer.convert_object_to_json(
                construction.military_unit
            ),
            'contractDate': get_date_string(construction.contract_date),
            'objectsAmount': construction.object_amount,
            'plannedDate': get_date_string(construction.planned_date),
            'constructionType': ConstructionTypeSerializer.convert_object_to_json(
                construction.type
            ),
            'locationType': LocationTypeSerializer.convert_object_to_json(
                construction.location_type
            ),
            'constructionCompany': ConstructionCompanySerializer.convert_object_to_json(
                construction.construction_company
            ),
            'oksm': OKSMSerializer.convert_object_to_json(
                construction.oksm
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
            'location': LocationSerializer.convert_object_to_json(
                construction.location
            ),
        }

    def convert_list_to_json(self, constructions: list) -> list:
        return list(map(self.convert_object_to_json, constructions))
