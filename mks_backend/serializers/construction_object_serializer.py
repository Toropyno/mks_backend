from mks_backend.models.construction_objects import ConstructionObjects


class ConstructionObjectSerializer:

    def convert_object_to_json(self, construction_object):
        construction_object_dict = {
            'id': construction_object.construction_objects_id,
            'constructionId': construction_object.construction_id,
            'objectCode': construction_object.object_code,
            'objectName': construction_object.object_name,
            'zonesId': construction_object.zones_id,
            'objectCategoriesListId': construction_object.object_categories_list_id,
            'plannedDate': construction_object.planned_date,
            'weight': construction_object.weight,
            'generalPlanNumber': construction_object.generalplan_number,
            'buildingVolume': construction_object.building_volume,
            'floorsAmount': construction_object.floors_amount,
            'constructionStagesId': construction_object.construction_stages_id,
        }
        return construction_object_dict

    def convert_list_to_json(self, construction_objects):
        return list(map(self.convert_object_to_json, construction_objects))


    def convert_schema_to_object(self, schema):
        construction_object = ConstructionObjects()
        if 'id' in schema:
            construction_object.construction_objects_id = schema['id']

        construction_object.construction_id = schema['constructionId']
        construction_object.object_code = schema['objectCode']
        construction_object.object_name = schema['objectName']
        construction_object.zones_id = schema['zonesId']
        construction_object.object_categories_list_id = schema['objectCategoriesListId']
        construction_object.planned_date = schema['plannedDate']
        construction_object.weight = schema['weight']
        construction_object.generalplan_number = schema['generalPlanNumber']
        construction_object.building_volume = schema['buildingVolume']
        construction_object.floors_amount = schema['floorsAmount']
        construction_object.construction_stages_id = schema['constructionStagesId']
        return construction_object