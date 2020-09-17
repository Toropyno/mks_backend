from pyramid.request import Request
from pyramid.view import view_config

from mks_backend.serializers.location import LocationSerializer
from mks_backend.services.location import LocationService


class LocationController:

    def __init__(self, request: Request):
        self.request = request
        self.service = LocationService()
        self.serializer = LocationSerializer()

    @view_config(route_name='get_locations', renderer='json')
    def get_all_locations(self):
        locations = self.service.get_all_locations()
        return self.serializer.convert_list_to_json(locations)
