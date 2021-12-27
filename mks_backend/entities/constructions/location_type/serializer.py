from .model import LocationType

from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.errors import serialize_error_handler


class LocationTypeSerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, location_type: LocationType) -> dict:
        return {
            'id': location_type.location_types_id,
            'fullName': location_type.fullname
        }

    def convert_schema_to_object(self, schema: dict) -> LocationType:
        location_type = LocationType()

        location_type.location_types_id = schema.get('id')
        location_type.fullname = schema.get('fullName')

        return location_type
