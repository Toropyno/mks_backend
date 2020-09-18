from pyramid.request import Request
from pyramid.view import view_config

from mks_backend.serializers.military_unit import MilitaryUnitSerializer
from mks_backend.services.military_unit import MilitaryUnitService


class MilitaryUnitController:

    def __init__(self, request: Request):
        self.request = request
        self.service = MilitaryUnitService()
        self.serializer = MilitaryUnitSerializer()

    @view_config(route_name='get_military_units', renderer='json')
    def get_all_military_units(self) -> list:
        root_military_units = self.service.get_root_military_units()
        return self.serializer.convert_list_to_json_tree(root_military_units)
