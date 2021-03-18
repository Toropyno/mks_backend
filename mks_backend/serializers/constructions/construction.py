from mks_backend.models.constructions import Construction

from mks_backend.serializers.oksm import OKSMSerializer
from mks_backend.serializers.coordinate import CoordinateSerializer
from mks_backend.serializers.military_unit import MilitaryUnitSerializer
from mks_backend.serializers.constructions.commision import CommissionSerializer
from mks_backend.serializers.organizations.organization import OrganizationSerializer
from mks_backend.serializers.constructions.location_type import LocationTypeSerializer
from mks_backend.serializers.construction_company import ConstructionCompanySerializer
from mks_backend.serializers.constructions.construction_type import ConstructionTypeSerializer
from mks_backend.serializers.constructions.construction_dynamic import ConstructionDynamicSerializer
from mks_backend.serializers.constructions.construction_category import ConstructionCategorySerializer
from mks_backend.serializers.constructions.construction_subcategory import ConstructionSubcategorySerializer

from mks_backend.serializers.utils.date_and_time import get_date_string


class ConstructionSerializer:

    def convert_list_to_json(self, constructions: list) -> list:
        return list(map(self.to_json, constructions))

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
            'department': construction.department,
            'officer': construction.officer,
            'actuallyEntered': construction.actually_entered,
            'readiness': construction.readiness,
            'technicalSpec': construction.technical_spec,
            'priceCalc': construction.price_calc,
            'deletionMark': construction.deletion_mark,
            'subcategory': subcategory,
            'isCritical': construction.is_critical,
            'objectsAmount': construction.object_amount,
            'note': construction.note,
            'plannedDate': get_date_string(construction.planned_date),

            'constructionType': ConstructionTypeSerializer.convert_object_to_json(construction.construction_type),
            'locationType': LocationTypeSerializer.convert_object_to_json(construction.location_type),
            'category': ConstructionCategorySerializer.to_short_json(construction.construction_category),
            'commission': CommissionSerializer.convert_object_to_json(construction.commission),
            'constructionCompany': ConstructionCompanySerializer.convert_object_to_json(construction.construction_company),
            'militaryUnit': MilitaryUnitSerializer.convert_object_to_json(construction.military_unit),
            'militaryDistrict': MilitaryUnitSerializer.convert_object_to_json(construction.military_district),
            'organization': OrganizationSerializer.to_simple_json(construction.organization),
            'dynamic': ConstructionDynamicSerializer.to_json(construction.dynamic),

            'fias': construction.fias,
            'address': construction.address_full,
            'coordinate': CoordinateSerializer.convert_object_to_json(construction.coordinate),
            'oksm': OKSMSerializer.convert_object_to_json(construction.oksm),
        }

        return construction_json
