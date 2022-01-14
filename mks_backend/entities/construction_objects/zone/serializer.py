from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.entities.construction_objects.object_category import ObjectCategorySerializer
from mks_backend.errors import serialize_error_handler

from .model import Zone


class ZoneSerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, zone: Zone) -> dict:
        return {
            'id': zone.zones_id,
            'fullName': zone.fullname,
            'categories': [
                ObjectCategorySerializer.to_json(category)
                for category in zone.object_categories
            ],
        }
