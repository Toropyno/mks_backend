from .model import Construction

from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.entities.oksm import OKSMSerializer
from mks_backend.entities.coordinate import CoordinateSerializer
from mks_backend.entities.military_unit import MilitaryUnitSerializer
from mks_backend.entities.constructions.commission import CommissionSerializer
from mks_backend.entities.organizations.organization import OrganizationSerializer
from mks_backend.entities.construction_company import ConstructionCompanySerializer
from mks_backend.entities.constructions.location_type import LocationTypeSerializer
from mks_backend.entities.constructions.construction_type import ConstructionTypeSerializer
from mks_backend.entities.constructions.construction_dynamic import ConstructionDynamicSerializer
from mks_backend.entities.constructions.construction_category import ConstructionCategorySerializer
from mks_backend.entities.constructions.construction_subcategory import ConstructionSubcategorySerializer

from mks_backend.utils.decimal import decimal_to_str
from mks_backend.utils.date_and_time import get_date_string
from mks_backend.entities.constructions.critical_category import CriticalCategorySerializer


class ConstructionSerializer(BaseSerializer):

    def to_json(self, construction: Construction) -> dict:
        if construction.subcategories_list:
            subcategory = ConstructionSubcategorySerializer.to_json(
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
            'readiness': decimal_to_str(construction.readiness),
            'technicalSpec': construction.technical_spec,
            'priceCalc': construction.price_calc,
            'deletionMark': construction.deletion_mark,
            'subcategory': subcategory,
            'isCritical': construction.is_critical,
            'objectsAmount': construction.object_amount,
            'note': construction.note,
            'plannedDate': get_date_string(construction.planned_date),

            'constructionType': ConstructionTypeSerializer.to_json(construction.construction_type),
            'locationType': LocationTypeSerializer.to_json(construction.location_type),
            'category': ConstructionCategorySerializer.to_short_json(construction.construction_category),
            'commission': CommissionSerializer.to_json(construction.commission),
            'constructionCompany': ConstructionCompanySerializer.to_json(
                construction.construction_company
            ),
            'militaryUnit': MilitaryUnitSerializer.to_json(construction.military_unit),
            'militaryDistrict': MilitaryUnitSerializer.to_json(construction.military_district),
            'organization': OrganizationSerializer.to_simple_json(construction.organization),
            'dynamic': ConstructionDynamicSerializer.to_json(construction.dynamic),

            'fias': construction.fias,
            'address': construction.address_full,
            'coordinate': CoordinateSerializer.to_json(construction.coordinate),
            'oksm': OKSMSerializer.to_json(construction.oksm),
            'criticalCategory': CriticalCategorySerializer.to_json(
                construction.critical_category
            )
        }

        return construction_json
