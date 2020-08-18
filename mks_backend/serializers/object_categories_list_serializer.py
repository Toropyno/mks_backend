class ObjectCategoriesListSerializer:

    def convert_object_to_json(self, object_categories_list):
        object_categories_list_dict = {
            'id': object_categories_list.object_categories_list_id,
            'zonesId': object_categories_list.zones_id,
            'objectCategoriesId': object_categories_list.object_categories_id,
        }
        return object_categories_list_dict

    def convert_list_to_json(self, object_categories_lists):
        return list(map(self.convert_object_to_json, object_categories_lists))
