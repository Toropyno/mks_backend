from mks_backend.errors import serialize_error_handler
from mks_backend.models.coordinate import Coordinate


class CoordinateSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, coordinate: Coordinate) -> dict:
        return {
            'id': coordinate.coordinates_id,
            'latitude': coordinate.latitude,
            'longitude': coordinate.longitude,
            'zoom': coordinate.zoom,
        }

    def convert_list_to_json(self, coordinates: list) -> list:
        return list(map(self.convert_object_to_json, coordinates))

    def convert_schema_to_object(self, schema: dict) -> Coordinate:
        if schema['latitude'] and schema['longitude'] and schema['zoom']:
            coordinate = Coordinate()
            if 'coordinateId' in schema:
                coordinate.coordinates_id = schema['coordinateId']

            coordinate.latitude = schema['latitude']
            coordinate.longitude = schema['longitude']
            coordinate.zoom = schema['zoom']
        else:
            coordinate = None
        return coordinate
