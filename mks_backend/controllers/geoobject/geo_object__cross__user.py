from pyramid.request import Request
from pyramid.view import view_defaults, view_config

from mks_backend.services.geoobject.geo_object__cross__user import GeoObjectCrossUserService


@view_defaults(renderer='json')
class GeoObjectCrossUser:

    def __init__(self, request: Request):
        self.request = request
        self.service = GeoObjectCrossUserService()

        #self.serializer = GeoObjectSerializer()
        # self.schema = MeetingSchema()
       # self.coordinate_serializer = CoordinateSerializer()