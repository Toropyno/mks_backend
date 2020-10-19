from pyramid.request import Request
from pyramid.view import view_defaults, view_config

from mks_backend.controllers.fias_entity.fias import get_fias_response, FIASController
from mks_backend.services.fias_entity.fias import get_addresses_from_response
from mks_backend.services.fias_entity.remaining_address import RemainingAddressService


@view_defaults(renderer='json')
class RemainingAddressController:

    def __init__(self, request: Request):
        self.request = request
        self.service = RemainingAddressService()
        self.fias_controller = FIASController(self.request)

    @view_config(route_name='get_remaining_addresses')
    def get_remaining_addresses(self):
        """
        Get remaining_address: 'ул ', 'ул. ', ' пер ', ' пер. ', ' ш ', ' ш. ', ' кв-л ', ' тер ', 'мкр ', ' тер. ',
                                'мкр. ', 'пр-кт '
        """
        text = self.request.matchdict['text']
        self.service.set_text(text)

        fias = self.fias_controller.get_fias_serialized()
        subject = fias.subject
        district = fias.district
        city = fias.city
        locality = fias.locality
        # subject = 'обл Белгородская'
        # district = 'р-н Белгородский'
        # city = 'пгт Разумное'
        # locality = None

        if city or locality is not None:
            search_text = self.service.get_search_text(
                {
                    'subject': subject,
                    'district': district,
                    'city': city,
                    'locality': locality,
                }
            )

            addresses = get_addresses_from_response(get_fias_response(search_text))
            return self.service.get_streets_houses(addresses)
