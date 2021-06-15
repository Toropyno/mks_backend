from uuid import uuid4

from mks_backend.errors import serialize_error_handler
from mks_backend.models.geoobject.geo_object import GeoObject
from mks_backend.models.geoobject.geo_object__cross__user import GeoObjectCrossUser
from mks_backend.serializers.coordinate import CoordinateSerializer
from mks_backend.serializers.geoobject.geo_style import GeoStyleSerialaizer


class GeoObjectSerializer:

    def to_object(self, dict: dict) -> GeoObject:
        geo_object = GeoObject()
        geo_object.style_id = dict.get('styleId')
        geo_object.projection = dict.get('projection')
        geo_object.geo_object_id = dict.get('id')

        geo_object__cross__user = GeoObjectCrossUser()
        geo_object__cross__user.user = 1
        geo_object__cross__user.layer_id = dict.get('layerId',  str(uuid4()))
        geo_object__cross__user.object_id = dict.get('objectId', str(uuid4()))
        geo_object.geo_object__cross__user = [geo_object__cross__user]
        return geo_object

    @classmethod
    @serialize_error_handler
    def to_json(cls, geo_object: GeoObject,  geo_object__cross__user: GeoObjectCrossUser) -> dict:
        return {
            'originId': geo_object.geo_object_id,
            'style':  GeoStyleSerialaizer.convert_object_to_json(geo_object.style),
            'projection': geo_object.projection,
            'id': geo_object__cross__user.geo_objects__cross__user_id,
            'layerId': geo_object__cross__user.layer_id,
            'objectId': geo_object__cross__user.object_id,
            'coordinate': CoordinateSerializer.convert_object_to_json(geo_object.coordinate),
        }
