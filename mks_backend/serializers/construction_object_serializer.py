from mks_backend.models.construction_objects import ConstructionObjects


class ConstructionObjectSerializer:

    def convert_object_to_json(self, construction_object):
        construction_object_dict = {
            'constructionId': construction_object.construction_id,
            'id': construction_object.construction_objects_id,
            'code': construction_object.object_code,
            'name': construction_object.object_name,
            'zone': construction_object.zone.fullname,
            'category': construction_object.object_categories_list.object_categories_instance.fullname,
            'plannedDate': self.get_date_string(construction_object.planned_date),
            'weight': construction_object.weight,
            'generalPlanNumber': construction_object.generalplan_number,
            'buildingVolume': float(construction_object.building_volume),
            'floorsAmount': construction_object.floors_amount,
            'stage': construction_object.construction_stage.fullname,
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

    def get_date_string(self, date):
        return str(date.year) + ',' + str(date.month) + ',' + str(date.day)