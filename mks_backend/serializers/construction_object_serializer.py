class ConstructionObjectSerializer:

    def convert_object_to_json(self, construction_object):
        construction_object_dict = {
            'id': construction_object.construction_objects_id,
            'construction_id': construction_object.construction_id,
            'object_code': construction_object.object_code,
            'object_name': construction_object.object_name,
            'zones_id': construction_object.zones_id,
            'object_categories_list_id': construction_object.object_categories_list_id,
            'planned_date': construction_object.planned_date,
            'weight': construction_object.weight,
            'generalplan_number': construction_object.generalplan_number,
            'building_volume': construction_object.building_volume,
            'floors_amount': construction_object.floors_amount,
            'construction_stages_id': construction_object.construction_stages_id,
        }
        return construction_object_dict

    def convert_list_to_json(self, construction_objects):
        construction_objects_array = []

        for construction_object in construction_objects:
            construction_object_dict = self.convert_object_to_json(construction_object)
            construction_objects_array.append(construction_object_dict)

        return construction_objects_array
