from mks_backend.models.location_type import LocationType

from mks_backend.errors.serilize_error import serialize_error_handler


class LocationTypeSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, location_type: LocationType) -> dict:
        return {
            'id': location_type.location_types_id,
            'fullName': location_type.fullname
        }

    def convert_list_to_json(self, location_types: list) -> list:
        return list(map(self.convert_object_to_json, location_types))

    def convert_schema_to_object(self, schema: dict) -> LocationType:
        location_type = LocationType()

        location_type.location_types_id = schema.get('id')
        location_type.fullname = schema.get('fullName')

        return location_type
