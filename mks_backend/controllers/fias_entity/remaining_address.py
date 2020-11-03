from pyramid.request import Request
from pyramid.view import view_defaults, view_config

from mks_backend.controllers.fias_entity.fias import FIASController
from mks_backend.services.fias_entity.remaining_address import RemainingAddressService


@view_defaults(renderer='json')
class RemainingAddressController:

    def __init__(self, request: Request):
        self.request = request
        self.service = RemainingAddressService()
        self.controller_FIAS = FIASController(self.request)

    @view_config(route_name='create_remaining_addresses_hints')
    def create_remaining_addresses_hints(self):
        self.service.search_rem_address = self.request.matchdict['text']
        fias_post = self.controller_FIAS.get_fias_serialized()
        return self.service.create_remaining_addresses_hints(fias_post)
