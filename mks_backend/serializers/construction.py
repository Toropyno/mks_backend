from mks_backend.models.construction import Construction
from mks_backend.serializers.commision import CommissionSerializer
from mks_backend.serializers.construction_category import ConstructionCategorySerializer
from mks_backend.serializers.construction_company import ConstructionCompanySerializer
from mks_backend.serializers.construction_subcategory import ConstructionSubcategorySerializer
from mks_backend.serializers.construction_type import ConstructionTypeSerializer
from mks_backend.serializers.coordinate import CoordinateSerializer
from mks_backend.serializers.fias.fias import FIASSerializer
from mks_backend.serializers.location_type import LocationTypeSerializer
from mks_backend.serializers.military_unit import MilitaryUnitSerializer
from mks_backend.serializers.oksm import OKSMSerializer
from mks_backend.serializers.utils.date_and_time import get_date_string


class ConstructionSerializer:

    def to_json(self, construction: Construction) -> dict:
        if construction.subcategories_list:
            subcategory = ConstructionSubcategorySerializer.convert_object_to_json(
                construction.subcategories_list.subcategory
            )
        else:
            subcategory = None

        construction_json = {
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
            'fias': FIASSerializer.convert_object_to_json(
                construction.fias
            ),
            'address': 'Неформализованный адрес проекта',
            'note': 'Примечание к проекту',
            'coordinate': CoordinateSerializer.convert_object_to_json(
                construction.coordinate
            ),
        }

        construction_json.update(construction.calculated_fields)
        return construction_json

    def convert_list_to_json(self, constructions: list) -> list:
        return list(map(self.to_json, constructions))
