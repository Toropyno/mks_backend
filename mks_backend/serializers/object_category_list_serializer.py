from mks_backend.models.object_category_list import ObjectCategoryList
from mks_backend.serializers.zone_serializer import ZoneSerializer


class ObjectCategoryListSerializer:

    def convert_object_to_json(self, object_categories_list: ObjectCategoryList) -> dict:
        zone = ZoneSerializer.convert_object_to_json(object_categories_list.zone)

        object_categories_list_dict = {
            'id': object_categories_list.object_categories_list_id,
            'zone': zone,
            'category': {
                'id': object_categories_list.object_categories_id,
                'fullName': object_categories_list.object_categories_instance.fullname
            }
        }
        return object_categories_list_dict

    def convert_list_to_json(self, object_categories_lists: list) -> list:
        return list(map(self.convert_object_to_json, object_categories_lists))

    def convert_schema_to_object(self, schema: dict) -> ObjectCategoryList:
        object_categories_list = ObjectCategoryList()
        if 'id' in schema:
            object_categories_list.object_categories_list_id = schema['id']

        object_categories_list.zones_id = schema['zone']
        object_categories_list.object_categories_id = schema['category']
        return object_categories_list
