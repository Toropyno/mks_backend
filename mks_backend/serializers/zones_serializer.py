from mks_backend.errors.serilize_error import serialize_error_handler
from mks_backend.models.zones import Zones
from mks_backend.serializers.object_category_serializer import ObjectCategorySerializer


class ZoneSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, zone):
        categories = []

        for object_categories_list in zone.object_categories_list:
            object_category = ObjectCategorySerializer.convert_object_to_json(
                object_categories_list.object_categories_instance
            )
            categories.append({
                'listID': object_categories_list.object_categories_list_id,
                'fullName': object_category['fullName'],
            })

        zone_dict = {
            'id': zone.zones_id,
            'fullName': zone.fullname,
            'categories': categories,
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
