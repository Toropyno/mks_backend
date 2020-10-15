from pyramid.request import Request
from pyramid.view import view_defaults, view_config

from mks_backend.controllers.fias_entity.fias import get_fias_response
from mks_backend.services.fias_entity.city import CityOrLocalityService
from mks_backend.services.fias_entity.fias import get_addresses_from_responce


@view_defaults(renderer='json')
class CityController:

    def __init__(self, request: Request):
        self.request = request
        self.service = CityOrLocalityService()

    @view_config(route_name='get_cities')
    def get_cities(self):
        cities = self.get_city_or_locality()
        self.service.set_city_or_locality(['г.', 'г ', ' город '])
        return cities

    def get_city_or_locality(self):
        text = self.request.matchdict['text']
        self.service.set_text(text)
        search_text = text
        subject = None
        district = None
        if district is not None:
            search_text = subject + ', ' + district + ', ' + search_text
        elif subject is not None:
            search_text = subject + ', ' + search_text
        addresses = get_addresses_from_responce(get_fias_response(search_text))
        cities = self.service.get_cities_or_localities(addresses, district, subject, text)
        return cities
