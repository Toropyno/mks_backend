from pyramid.view import view_config
from pyramid.request import Request

from mks_backend.services.military_unit import MilitaryUnitService
from mks_backend.serializers.military_unit import MilitaryUnitSerializer


class MilitaryUnitController:

    def __init__(self, request: Request):
        self.request = request
        self.service = MilitaryUnitService()
        self.serializer = MilitaryUnitSerializer()

    @view_config(route_name='military_units', request_method='GET', renderer='json')
    def get_all_military_units(self) -> list:
        root_military_units = self.service.get_root_military_units()
        return self.serializer.convert_list_to_json_tree(root_military_units)
