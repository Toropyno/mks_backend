from datetime import date as Date
from mks_backend.models.construction_objects import ConstructionObjects

from mks_backend.serializers.zones_serializer import ZoneSerializer
from mks_backend.serializers.object_category_serializer import ObjectCategorySerializer
from mks_backend.serializers.construction_stage_serializer import ConstructionStageSerializer


class ConstructionObjectSerializer:

    def convert_object_to_json(self, construction_object: ConstructionObjects) -> dict:
        zone = ZoneSerializer.convert_object_to_json(construction_object.zone)

        if construction_object.object_categories_list:
            category = ObjectCategorySerializer.convert_object_to_json(
                construction_object.object_categories_list.object_categories_instance
            )
        else:
            category = None

        stage = ConstructionStageSerializer.convert_object_to_json(construction_object.construction_stage)

        building_volume = float(construction_object.building_volume) if construction_object.building_volume else None

        construction_object_dict = {
            'projectId': construction_object.construction_id,
            'id': construction_object.construction_objects_id,
            'code': construction_object.object_code,
            'name': construction_object.object_name,
            'zone': zone,
            'category': category,
            'plannedDate': self.get_date_string(construction_object.planned_date),
            'weight': construction_object.weight,
            'generalPlanNumber': construction_object.generalplan_number,
            'buildingVolume': building_volume,
            'floorsAmount': construction_object.floors_amount,
            'stage': stage,
        }
        return construction_object_dict

    def convert_list_to_json(self, construction_objects: list) -> list:
        return list(map(self.convert_object_to_json, construction_objects))

    def convert_schema_to_object(self, schema: dict) -> ConstructionObjects:
        construction_object = ConstructionObjects()
        if 'id' in schema:
            construction_object.construction_objects_id = schema['id']

        construction_object.construction_id = schema['projectId']
        construction_object.object_code = schema['code']
        construction_object.object_name = schema['name']
        construction_object.zones_id = schema['zone']
        construction_object.object_categories_list_id = schema['category']
        construction_object.planned_date = schema['plannedDate']
        construction_object.weight = schema['weight']
        construction_object.generalplan_number = schema['generalPlanNumber']
        construction_object.building_volume = schema['buildingVolume']
        construction_object.floors_amount = schema['floorsAmount']
        construction_object.construction_stages_id = schema['stage']
        return construction_object

    def get_date_string(self, date: Date) -> str:
        return str(date.year) + ',' + str(date.month) + ',' + str(date.day)
