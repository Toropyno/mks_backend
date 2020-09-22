from mks_backend.models.construction_object import ConstructionObject

from mks_backend.serializers._date_utils import get_date_string
from mks_backend.serializers.construction_stage import ConstructionStageSerializer
from mks_backend.serializers.object_category import ObjectCategorySerializer
from mks_backend.serializers.zone import ZoneSerializer
from mks_backend.serializers.location import LocationSerializer
# from mks_backend.serializers.realty_type import RealtyTypeSerializer

from mks_backend.services.construction_progress import ConstructionProgressService


class ConstructionObjectSerializer:

    def __init__(self):
        self.construction_progress_service = ConstructionProgressService()
        # self.realty_type_service = RealtyTypeSerializer()

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

        location = LocationSerializer.convert_object_to_json(construction_object.location)
        #
        # realty_type = self.realty_type_service.convert_object_to_json(construction_object.realty_type)

        construction_progress = self.construction_progress_service.get_construction_progress_for_construction_objects()
        if construction_progress is not None:
            construction_progress = {
                'readiness': float(construction_progress.readiness),
                'people': construction_progress.people,
                'equipment': construction_progress.equipment,
                # 'progressStatusesId': construction_progress.progress_statuses_id,
            }

        fact_date = construction_object.fact_date
        if fact_date is not None:
            fact_date = get_date_string(fact_date)

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
            'location': location,
            # 'realtyType': realty_type,
            'factDate': fact_date,
            'constructionProgress': construction_progress,
        }
        return construction_object_dict

    def convert_list_to_json(self, construction_objects: list) -> list:
        return list(map(self.convert_object_to_json, construction_objects))
