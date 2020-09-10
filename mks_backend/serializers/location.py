from mks_backend.models.location import Location
from mks_backend.errors.serilize_error import serialize_error_handler


class LocationSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, location: Location) -> dict:
        return {
            'id': location.id,
            'latitude': location.latitude,
            'longitude': location.longitude,
            'zoom': location.zoom,
        }

    @classmethod
    def convert_list_to_json(cls, locations: list) -> list:
        return list(map(cls.convert_object_to_json, locations))

    @classmethod
    def convert_schema_to_object(cls, schema: dict) -> Location:
        location = Location()
        if 'locationId' in schema:
            location.id = schema['locationId']

        location.latitude = schema['latitude']
        location.longitude = schema['longitude']
        location.zoom = schema['zoom']
        return location
