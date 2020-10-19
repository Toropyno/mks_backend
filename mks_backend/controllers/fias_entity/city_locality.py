from pyramid.request import Request
from pyramid.view import view_defaults, view_config

from mks_backend.controllers.fias_entity.fias import get_fias_response
from mks_backend.services.fias_entity.city_locality import CityLocalityService
from mks_backend.services.fias_entity.fias import get_addresses_from_responce


@view_defaults(renderer='json')
class CityLocalityController:

    def __init__(self, request: Request):
        self.request = request
        self.service = CityLocalityService()

    @view_config(route_name='get_cities')
    def get_cities(self):
        return self.get_cities_or_localities(['г.', 'г ', ' город '])

    @view_config(route_name='get_localities')
    def get_localities(self):
        return self.get_cities_or_localities(
            ['пгт. ', 'пгт ', 'п. ', 'п ', 'д. ', 'д ', 'с. ', 'с ', 'п. им. ', 'п им ', 'ст-ца ', ' x ', ' тер ']
        )

    def get_cities_or_localities(self, socr_names):
        self.service.set_socr_names(socr_names)
        self.service.set_text(self.request.matchdict['text'])
        subject = None
        district = None
        search_text = self.service.get_search_text(district, subject)
        addresses = get_addresses_from_responce(get_fias_response(search_text))
        return self.service.get_cities_or_localities(addresses, district, subject)
