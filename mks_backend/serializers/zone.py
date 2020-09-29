from mks_backend.errors.serilize_error import serialize_error_handler
from mks_backend.models.zone import Zone
from mks_backend.serializers.object_category import ObjectCategorySerializer


class ZoneSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, zone: Zone) -> dict:
        return {
            'id': zone.zones_id,
            'fullName': zone.fullname,
            'categories': [
                ObjectCategorySerializer.convert_object_to_json(category)
                for category in zone.object_categories
            ],
        }

    def convert_list_to_json(self, zones: list) -> list:
        return list(map(self.convert_object_to_json, zones))
