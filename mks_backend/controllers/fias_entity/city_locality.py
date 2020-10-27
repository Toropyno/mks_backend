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

    @view_config(route_name='cities_hints')
    def cities_hints(self):
        """
            cities: 'г. ', 'г ', 'город '
        """
        self.service.set_sity_socr_names()
        return self.get_cities_or_localities()

    @view_config(route_name='localities_hints')
    def localities_hints(self):
        """
            localities: 'пгт. ', 'пгт ', 'п. ', 'п ', 'д. ', 'д ', 'с. ', 'с ', 'п. им. ', 'п им ', 'ст-ца ',
                        'х ', 'х. ', 'рп ', 'рп. '
        """
        self.service.set_locality_socr_names()
        return self.get_cities_or_localities()

    def get_cities_or_localities(self) -> list:
        self.service.search_address = self.request.matchdict['text']
        fias_post = self.controller_FIAS.get_fias_serialized()
        return self.service.get_cities_or_localities(fias_post)
