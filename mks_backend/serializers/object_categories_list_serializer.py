from mks_backend.models.object_categories_list import ObjectCategoriesList


class ObjectCategoriesListSerializer:

    def convert_object_to_json(self, object_categories_list):
        object_categories_list_dict = {
            'id': object_categories_list.object_categories_list_id,
            'zone': {
                'id': object_categories_list.zones_id,
                'fullName': object_categories_list.zone.fullname
            },
            'category': {
                'id': object_categories_list.object_categories_id,
                'fullName': object_categories_list.object_categories_instance.fullname
            }
        }
        return object_categories_list_dict

    def convert_list_to_json(self, object_categories_lists):
        return list(map(self.convert_object_to_json, object_categories_lists))

    def convert_schema_to_object(self, schema):
        object_categories_list = ObjectCategoriesList()
        if 'id' in schema:
            object_categories_list.object_categories_list_id = schema['id']

        object_categories_list.zones_id = schema['zoneId']
        object_categories_list.object_categories_id = schema['objectCategoriesId']
        return object_categories_list
