from pyramid.view import view_config

from mks_backend.services.military_unit_service import MilitaryUnitService
from mks_backend.serializers.military_unit_serializer import MilitaryUnitSerializer


class MilitaryUnitController:

    def __init__(self, request):
        self.request = request
        self.service = MilitaryUnitService()
        self.serializer = MilitaryUnitSerializer()

    @view_config(route_name='military_units', request_method='GET', renderer='json')
    def get_all_military_units(self):
        root_military_units = self.service.get_root_military_units()
        json = self.serializer.convert_list_to_json_tree(root_military_units)
        return json
