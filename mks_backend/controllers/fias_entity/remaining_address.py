from pyramid.request import Request
from pyramid.view import view_defaults, view_config

from mks_backend.controllers.fias_entity.fias import FIASController
from mks_backend.services.fias_entity.remaining_address import RemainingAddressService

from mks_backend.errors.fias_error import get_locality_error, fias_error_handler


@view_defaults(renderer='json')
class RemainingAddressController:

    def __init__(self, request: Request):
        self.request = request
        self.service = RemainingAddressService()
        self.controller_FIAS = FIASController(self.request)

    @fias_error_handler
    @view_config(route_name='create_remaining_addresses_hints')
    def create_remaining_addresses_hints(self):
        """
            remaining_address: 'ул ', 'ул. ', 'пер ', 'пер. ', 'ш ', 'ш. ', 'кв-л ', 'тер ', 'тер. ', 'мкр ', 'мкр. ',
                               'пр-кт ', 'б-р ', 'б-р. ', 'проезд ', 'проезд. ', 'туп ', 'туп. ', 'пл ', 'пл. ',
                               'мост ', 'снт '
        """
        self.service.search_rem_address = self.request.matchdict['text']

        fias_post = self.controller_FIAS.get_fias_serialized()

        remaining_addresses = self.service.create_remaining_addresses_hints(fias_post)
        if remaining_addresses:
            return list(remaining_addresses)
        else:
            return get_locality_error()
