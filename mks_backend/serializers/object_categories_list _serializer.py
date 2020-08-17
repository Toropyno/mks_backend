class ObjectCategoriesListSerializer:

    def convert_object_to_json(self, object_categories_list):
        object_categories_list_dict = {
            'id': object_categories_list.object_categories_lists_id,
            'zonesId': object_categories_list.zones_id,
            'objectCategoriesId': object_categories_list.object_categories_id,
        }
        return object_categories_list_dict

    def convert_list_to_json(self, object_categories_lists):
        object_categories_lists_array = []

        for object_categories_list in object_categories_lists:
            object_categories_list_dict = self.convert_object_to_json(object_categories_list)
            object_categories_lists_array.append(object_categories_list_dict)

        return object_categories_lists_array
