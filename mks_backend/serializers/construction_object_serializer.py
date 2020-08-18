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
            'stage': {
                'fullname': construction_object.construction_stage.fullname,
                'id': construction_object.construction_stage_id,
                'code': construction_object.construction_stage.code,
            }
        }
        return construction_object_dict

    def convert_list_to_json(self, construction_objects):
        return list(map(self.convert_object_to_json, construction_objects))

    def get_date_string(self, date):
        return str(date.year) + ',' + str(date.month) + ',' + str(date.day)
