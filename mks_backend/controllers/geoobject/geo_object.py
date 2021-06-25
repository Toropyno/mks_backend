from pyramid.request import Request
from pyramid.view import view_defaults, view_config

from mks_backend.serializers.coordinate import CoordinateSerializer
from mks_backend.serializers.geoobject.geo_object import GeoObjectSerializer
from mks_backend.services.geoobject.geo_object import GeoObjectService


@view_defaults(renderer='json')
class GeoObjectController:

    def __init__(self, request: Request):
        self.request = request
        self.service = GeoObjectService()

        self.serializer = GeoObjectSerializer()
        #self.schema = MeetingSchema()
        self.coordinate_serializer = CoordinateSerializer()

    @view_config(route_name='add_geo_object')
    def add_construction(self):
        #construction_deserialized = self.schema.deserialize(self.request.json_body)
        geo_object = self.serializer.to_object(self.request.json_body)
        coordinate = self.coordinate_serializer.convert_schema_to_object(self.request.json_body)
        #construction = self.service.convert_schema_to_object(construction_deserialized)
        geo_object.coordinate = coordinate
       #  geo_object.coordinate = coordinate

        self.service.add_geo_object(geo_object)
        return {'id': geo_object.geo_object_id}