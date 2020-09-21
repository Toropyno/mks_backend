from mks_backend.models.construction_object import ConstructionObject
from mks_backend.serializers._date_utils import get_date_string
from mks_backend.serializers.construction_progress import ConstructionProgressSerializer

from mks_backend.serializers.construction_stage import ConstructionStageSerializer
from mks_backend.serializers.object_category import ObjectCategorySerializer
from mks_backend.serializers.zone import ZoneSerializer
# from mks_backend.serializers.coordinate import CoordinateSerializer
# from mks_backend.serializers.realty_type import RealtyTypeSerializer
from mks_backend.services.construction_progress import ConstructionProgressService


class ConstructionObjectSerializer:

    def convert_object_to_json(self, construction_object: ConstructionObject) -> dict:
        zone = ZoneSerializer.convert_object_to_json(construction_object.zone)

        if construction_object.object_categories_list:
            category = ObjectCategorySerializer.convert_object_to_json(
                construction_object.object_categories_list.object_category
            )
        else:
            category = None

        stage = ConstructionStageSerializer.convert_object_to_json(construction_object.construction_stage)

        building_volume = float(construction_object.building_volume) if construction_object.building_volume else None

        # coordinate = CoordinateSerializer.convert_object_to_json(construction_object.coordinate)
        #
        # realty_type = RealtyTypeSerializer.convert_object_to_json(construction_object.realty_type)

        progress_for_objects = ConstructionProgressService.get_construction_progress_for_construction_objects()
        construction_progress = ConstructionProgressSerializer.convert_object_to_json(progress_for_objects)
        # construction_progress = {
        #     'readiness': construction_progress['readiness'],
        #     'people': construction_progress['people'],
        #     'equipment': construction_progress['equipment]',
        #     'progressStatusesId': construction_progress['progressStatusesId'],
        # }

        construction_object_dict = {
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
            'stage': stage,
            # 'location': coordinate,
            # 'realtyType': realty_type,
            'factDate': get_date_string(construction_object.fact_date),
            'constructionProgress': construction_progress,
        }
        return construction_object_dict

    def convert_list_to_json(self, construction_objects: list) -> list:
        return list(map(self.convert_object_to_json, construction_objects))
