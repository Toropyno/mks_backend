from pyramid.request import Request
from pyramid.view import view_defaults, view_config

from mks_backend.controllers.fias_entity.fias import get_fias_response
from mks_backend.services.fias_entity.fias import get_addresses_from_responce
from mks_backend.services.fias_entity.streets_houses import StreetHouseService


@view_defaults(renderer='json')
class StreetHouseController:

    def __init__(self, request: Request):
        self.request = request
        self.service = StreetHouseService()

    @view_config(route_name='get_streets_houses')
    def get_streets_houses(self):
        """
        Get district: 'ул ', 'ул. ', ' пер ', ' пер. ', ' ш ', ' ш. ', ' кв-л ', ' тер ', 'мкр ', ' тер. ', 'мкр. ',
                      'пр-кт '
        """
        text = self.request.matchdict['text']
        self.service.set_text(text)

        subject = None
        district = None
        city = None
        locality = None

        if city or locality is not None:
            search_text = self.service.get_search_text(
                {
                    'subject': subject,
                    'district': district,
                    'city': city,
                    'locality': locality,
                }
            )

            addresses = get_addresses_from_responce(get_fias_response(search_text))
            return self.service.get_streets_houses(addresses)
