from pyramid.request import Request
from pyramid.view import view_defaults, view_config

from mks_backend.controllers.fias_entity.fias import FIASController
from mks_backend.services.fias_entity.city_locality import CityLocalityService
from mks_backend.services.fias_entity.fias import FIASService


@view_defaults(renderer='json')
class CityLocalityController:

    def __init__(self, request: Request):
        self.request = request
        self.service = CityLocalityService()
        self.controller_FIAS = FIASController(self.request)
        self.service_FIAS = FIASService()

    @view_config(route_name='get_cities')
    def get_cities(self):
        self.service.socr_names = ['г. ', 'г ', 'город ']
        return self.get_cities_or_localities()

    @view_config(route_name='get_localities')
    def get_localities(self):
        self.service.socr_names = ['пгт. ', 'пгт ', 'п. ', 'п ', 'д. ', 'д ', 'с. ', 'с ', 'п. им. ', 'п им ', 'ст-ца ',
                                   'х ', 'х. ', 'рп ', 'рп. ']
        return self.get_cities_or_localities()

    def get_cities_or_localities(self) -> list:
        self.service.search_address = self.request.matchdict['text']
        fias_post = self.controller_FIAS.get_fias_serialized()

        search_text = self.service.get_search_text(fias_post)
        addresses = self.service_FIAS.get_addresses_from_response(self.service_FIAS.get_fias_response(search_text))
        return self.service.get_cities_or_localities(addresses, fias_post)
