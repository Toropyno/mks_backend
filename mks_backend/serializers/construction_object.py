from mks_backend.models.construction_object import ConstructionObject
from mks_backend.serializers.construction_progress import ConstructionProgressSerializer
from mks_backend.serializers.construction_stage import ConstructionStageSerializer
from mks_backend.serializers.coordinate import CoordinateSerializer
from mks_backend.serializers.object_category import ObjectCategorySerializer
from mks_backend.serializers.realty_type import RealtyTypeSerializer
from mks_backend.serializers.utils.date_and_time import get_date_string
from mks_backend.serializers.zone import ZoneSerializer


class ConstructionObjectSerializer:

    def convert_object_to_json(self, construction_object: ConstructionObject) -> dict:
        zone = ZoneSerializer.convert_object_to_json(construction_object.zone)

        if construction_object.object_categories_list:
            category = ObjectCategorySerializer.convert_object_to_json(
                construction_object.object_categories_list.object_category
            )
        else:
            category = None

        building_volume = float(construction_object.building_volume) if construction_object.building_volume else None

        fact_date = construction_object.fact_date
        if fact_date is not None:
            fact_date = get_date_string(fact_date)

        construction_progress = construction_object.construction_progress
        if construction_progress:
            construction_progress = construction_progress[len(construction_progress)-1]
            construction_progress = ConstructionProgressSerializer().convert_object_to_json(construction_progress)

        construction_object = {
            'projectId': construction_object.construction_id,
            'id': construction_object.construction_objects_id,
            'code': construction_object.object_code,
            'name': construction_object.object_name,
            'zone': zone,
            'category': category,
            'plannedDate': get_date_string(construction_object.planned_date),
            'weight': construction_object.weight,
            'generalPlanNumber': construction_object.generalplan_number,
            'buildingVolume': building_volume,
            'floorsAmount': construction_object.floors_amount,
            'stage': ConstructionStageSerializer.convert_object_to_json(
                construction_object.construction_stage
            ),
            'coordinate': CoordinateSerializer.convert_object_to_json(
                construction_object.coordinate
            ),
            'realtyType': RealtyTypeSerializer.convert_object_to_json(
                construction_object.realty_type
            ),
            'factDate': fact_date,
            'constructionProgress': construction_progress,
        }
        return construction_object

    def convert_list_to_json(self, construction_objects: list) -> list:
        return list(map(self.convert_object_to_json, construction_objects))
