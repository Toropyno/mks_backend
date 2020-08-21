from mks_backend.models.construction_objects import ConstructionObjects


class ConstructionObjectSerializer:

    def convert_object_to_json(self, construction_object):
        construction_object_dict = {
            'projectId': construction_object.construction_id,
            'id': construction_object.construction_objects_id,
            'code': construction_object.object_code,
            'name': construction_object.object_name,
            'zone': {
                'id': construction_object.zone.zones_id,
                'fullName': construction_object.zone.fullname,
            },
            'category': {
                'id': construction_object.object_categories_list.object_categories_id,
                'fullName': construction_object.object_categories_list.object_categories_instance.fullname,
                'note': construction_object.object_categories_list.object_categories_instance.note
            },
            'plannedDate': self.get_date_string(construction_object.planned_date),
            'weight': construction_object.weight,
            'generalPlanNumber': construction_object.generalplan_number,
            'buildingVolume': float(construction_object.building_volume),
            'floorsAmount': construction_object.floors_amount,
            'stage': {
                'id': construction_object.construction_stage.construction_stages_id,
                'fullName': construction_object.construction_stage.fullname,
                'code': construction_object.construction_stage.code
            },
        }
        return construction_object_dict

    def convert_list_to_json(self, construction_objects):
        return list(map(self.convert_object_to_json, construction_objects))

    def convert_schema_to_object(self, schema):
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

    def get_date_string(self, date):
        return str(date.year) + ',' + str(date.month) + ',' + str(date.day)