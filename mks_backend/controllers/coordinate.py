from pyramid.request import Request
from pyramid.view import view_config

from mks_backend.serializers.coordinate import CoordinateSerializer
from mks_backend.services.coordinate import CoordinateService


class CoordinateController:

    def __init__(self, request: Request):
        self.request = request
        self.service = CoordinateService()
        self.serializer = CoordinateSerializer()

    @view_config(route_name='get_coordinates', renderer='json')
    def get_all_coordinates(self):
        coordinates = self.service.get_all_coordinates()
        return self.serializer.convert_list_to_json(coordinates)
