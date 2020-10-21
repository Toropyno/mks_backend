from pyramid.request import Request
from pyramid.view import view_defaults, view_config

from mks_backend.controllers.fias_entity.fias import FIASController
from mks_backend.services.fias_entity.city_locality import CityLocalityService


@view_defaults(renderer='json')
class CityLocalityController:

    def __init__(self, request: Request):
        self.request = request
        self.service = CityLocalityService()
        self.controller_FIAS = FIASController(self.request)

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
        return self.service.get_cities_or_localities(fias_post)
