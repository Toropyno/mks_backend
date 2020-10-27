from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.controllers.fias_entity.fias import FIASController
from mks_backend.services.fias_entity.api import FIASAPIService
from mks_backend.services.fias_entity.utils import get_search_address


@view_defaults(renderer='json')
class FIASAPIController:

    def __init__(self, request: Request):
        self.request = request
        self.service = FIASAPIService()
        self.controller_FIAS = FIASController(self.request)

    @view_config(route_name='fias_search_hints')
    def fias_search_hints(self):
        full_fias = self.controller_FIAS.get_full_fias_serialized()
        return self.service.get_fias_search(full_fias)

    @view_config(route_name='get_final_fias_address')
    def get_final_fias_address(self):
        fias = self.controller_FIAS.get_fias_serialized()
        search_address = get_search_address(fias)
        return self.service.get_final_fias_address(search_address)
