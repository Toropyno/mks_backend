from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .serializer import CoordinateSerializer
from .service import CoordinateService


@view_defaults(renderer='json')
class CoordinateController:

    def __init__(self, request: Request):
        self.request = request
        self.service = CoordinateService()
        self.serializer = CoordinateSerializer()

    @view_config(route_name='get_coordinates')
    def get_all_coordinates(self):
        coordinates = self.service.get_all_coordinates()
        return self.serializer.convert_list_to_json(coordinates)
