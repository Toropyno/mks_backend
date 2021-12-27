from .model import ConstructionObject

from mks_backend.utils.decimal import decimal_to_str
from mks_backend.utils.date_and_time import get_date_string

from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.entities.construction_objects.object_category import ObjectCategorySerializer
from mks_backend.entities.construction_objects.zone import ZoneSerializer
from mks_backend.entities.construction_objects.construction_stage import ConstructionStageSerializer
from mks_backend.entities.construction_objects.construction_progress import ConstructionProgressSerializer
from mks_backend.entities.construction_objects.realty_type import RealtyTypeSerializer
from mks_backend.entities.coordinate import CoordinateSerializer


class ConstructionObjectSerializer(BaseSerializer):

    def to_json(self, construction_object: ConstructionObject) -> dict:
        if construction_object.object_categories_list:
            category = ObjectCategorySerializer.to_json(
                construction_object.object_categories_list.object_category
            )
        else:
            category = None

        return {
            'projectId': construction_object.construction_id,
            'id': construction_object.construction_objects_id,
            'code': construction_object.object_code,
            'name': construction_object.object_name,
            'category': category,
            'factDate': get_date_string(construction_object.fact_date),
            'weight': decimal_to_str(construction_object.weight),
            'generalPlanNumber': construction_object.generalplan_number,
            'buildingVolume': decimal_to_str(construction_object.building_volume, scale=3),
            'floorsAmount': construction_object.floors_amount,
            'zone': ZoneSerializer.to_json(construction_object.zone),
            'stage': ConstructionStageSerializer.to_json(
                construction_object.construction_stage
            ),
            'coordinate': CoordinateSerializer.to_json(
                construction_object.coordinate
            ),
            'realtyType': RealtyTypeSerializer.to_json(
                construction_object.realty_type
            ),
            'constructionProgress': ConstructionProgressSerializer.to_json(
                construction_object.last_report
            ),
            'plannedDate': get_date_string(construction_object.planned_date),
        }
