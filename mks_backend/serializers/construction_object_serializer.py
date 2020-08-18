class ConstructionObjectSerializer:

    def convert_object_to_json(self, construction_object):
        construction_object_dict = {
            'id': construction_object.construction_objects_id,
            'constructionId': construction_object.construction_id,
            'objectCode': construction_object.object_code,
            'objectName': construction_object.object_name,
            'zonesId': construction_object.zones_id,
            'objectCategoriesListId': construction_object.object_categories_list_id,
            'plannedDate': self.get_date_string(construction_object.planned_date),
            'weight': construction_object.weight,
            'generalPlanNumber': construction_object.generalplan_number,
            'buildingVolume': float(construction_object.building_volume),
            'floorsAmount': construction_object.floors_amount,
            'constructionStagesId': construction_object.construction_stages_id,
        }
        return construction_object_dict

    def convert_list_to_json(self, construction_objects):
        return list(map(self.convert_object_to_json, construction_objects))

    def get_date_string(self, date):
        return str(date.year) + ',' + str(date.month) + ',' + str(date.day)
