from mks_backend.errors.serilize_error import serialize_error_handler
from mks_backend.models.zones import Zones
from mks_backend.serializers.object_category_serializer import ObjectCategorySerializer


class ZoneSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, zone):
        object_categories = [
            ObjectCategorySerializer.convert_object_to_json(object_categories_list.object_categories_instance)
            for object_categories_list in zone.object_categories_list
        ]

        object_categories_full_names = [(object_category['fullName']) for object_category in object_categories]
        all = []

        for object_categories_list in zone.object_categories_list:
            for object_categories_full_name in object_categories_full_names:
                all.append({
                    'objectCategoriesListId': object_categories_list.object_categories_list_id,
                    'objectCategoriesFullName': object_categories_full_name,
                })

        zone_dict = {
            'id': zone.zones_id,
            'fullName': zone.fullname,
            'categories': all,
        }
        return zone_dict

    def convert_list_to_json(self, zones):
        return list(map(self.convert_object_to_json, zones))

    def convert_schema_to_object(self, schema):
        zone = Zones()
        if 'id' in schema:
            zone.zones_id = schema['id']

        zone.fullname = schema['fullName']
        return zone
