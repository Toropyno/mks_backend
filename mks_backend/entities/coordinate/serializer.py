from .model import Coordinate

from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.errors import serialize_error_handler


class CoordinateSerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, coordinate: Coordinate) -> dict:
        return {
            'id': coordinate.coordinates_id,
            'latitude': coordinate.latitude,
            'longitude': coordinate.longitude,
            'zoom': coordinate.zoom,
        }

    def to_mapped_object(self, schema: dict) -> Coordinate:
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
