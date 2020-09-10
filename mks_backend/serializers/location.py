from mks_backend.models.location import Location
from mks_backend.errors.serilize_error import serialize_error_handler


class LocationSerializer:

    @serialize_error_handler
    def convert_object_to_json(self, location: Location) -> dict:
        return {
            'id': location.id,
            'latitude': location.latitude,
            'longitude': location.longitude,
            'zoom': location.zoom,
        }

    def convert_list_to_json(self, locations: list) -> list:
        return list(map(self.convert_object_to_json, locations))

    def convert_schema_to_object(self, schema: dict) -> Location:
        location = Location()
        if 'locationId' in schema:
            location.id = schema['locationId']

        location.latitude = schema['latitude']
        location.longitude = schema['longitude']
        location.zoom = schema['zoom']
        return location
