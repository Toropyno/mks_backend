from mks_backend.models.construction_objects.construction_object import ConstructionObject
from mks_backend.serializers.construction_objects.construction_progress import ConstructionProgressSerializer
from mks_backend.serializers.construction_objects.construction_stage import ConstructionStageSerializer
from mks_backend.serializers.coordinate import CoordinateSerializer
from mks_backend.serializers.construction_objects.object_category import ObjectCategorySerializer
from mks_backend.serializers.construction_objects.realty_type import RealtyTypeSerializer
from mks_backend.serializers.utils.date_and_time import get_date_string
from mks_backend.serializers.construction_objects.zone import ZoneSerializer


class ConstructionObjectSerializer:

    def convert_object_to_json(self, construction_object: ConstructionObject) -> dict:
        if construction_object.object_categories_list:
            category = ObjectCategorySerializer.convert_object_to_json(
                construction_object.object_categories_list.object_category
            )
        else:
            category = None

        building_volume = float(construction_object.building_volume) if construction_object.building_volume else None

        return {
            'projectId': construction_object.construction_id,
            'id': construction_object.construction_objects_id,
            'code': construction_object.object_code,
            'name': construction_object.object_name,
            'category': category,
            'plannedDate': get_date_string(construction_object.planned_date),
            'factDate': get_date_string(construction_object.fact_date),
            'weight': construction_object.weight,
            'generalPlanNumber': construction_object.generalplan_number,
            'buildingVolume': building_volume,
            'floorsAmount': construction_object.floors_amount,
            'zone': ZoneSerializer.convert_object_to_json(construction_object.zone),
            'stage': ConstructionStageSerializer.convert_object_to_json(
                construction_object.construction_stage
            ),
            'coordinate': CoordinateSerializer.convert_object_to_json(
                construction_object.coordinate
            ),
            'realtyType': RealtyTypeSerializer.convert_object_to_json(
                construction_object.realty_type
            ),
            'constructionProgress': ConstructionProgressSerializer.convert_object_to_json(
                construction_object.last_report
            ),
        }

    def convert_list_to_json(self, construction_objects: list) -> list:
        return list(map(self.convert_object_to_json, construction_objects))
