from pyramid.request import Request
from pyramid.view import view_defaults, view_config

from mks_backend.controllers.fias_entity.fias import FIASController
from mks_backend.services.fias_entity.fias import get_addresses_from_response, FIASService
from mks_backend.services.fias_entity.remaining_address import RemainingAddressService


@view_defaults(renderer='json')
class RemainingAddressController:

    def __init__(self, request: Request):
        self.request = request
        self.service = RemainingAddressService()
        self.controller_FIAS = FIASController(self.request)
        self.service_FIAS = FIASService()

    @view_config(route_name='get_remaining_addresses')
    def get_remaining_addresses(self):
        """
        Get remaining_address: 'ул ', 'ул. ', 'пер ', 'пер. ', 'ш ', 'ш. ', 'кв-л ', 'тер ', 'тер. ', 'мкр ', 'мкр. ',
                                'пр-кт ', 'б-р ', 'б-р. ', 'проезд ', 'проезд. ', 'туп ', 'туп. ', 'пл ', 'пл. '
        """
        search_rem_address = self.request.matchdict['text']
        self.service.search_rem_address = search_rem_address

        fias_post = self.controller_FIAS.get_fias_serialized()
        if fias_post.city or fias_post.locality is not None:
            search_text = self.service.get_search_text(fias_post)

            addresses = get_addresses_from_response(self.service_FIAS.get_fias_response(search_text))
            return self.service.get_remaining_addresses(addresses)
