from pyramid.request import Request
from pyramid.view import view_defaults, view_config

from mks_backend.serializers.geoobject.geo_style import GeoStyleSerialaizer
from mks_backend.services.geoobject.geo_style import GeoStyleService


@view_defaults(renderer='json')
class GeoStyleController:

    def __init__(self, request: Request):
        self.request = request
        self.service = GeoStyleService()
        self.serializer = GeoStyleSerialaizer()
        #self.schema = MeetingSchema()

    @view_config(route_name='get_geo_style')
    def get_geo_style(self):
        id = self.request.matchdict['id']
        style = self.service.get_geo_style_by_id(id)
        return self.serializer.convert_object_to_json(style)
