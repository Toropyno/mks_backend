from pyramid.request import Request
from pyramid.view import view_defaults, view_config

from mks_backend.controllers.fias_entity.fias import get_fias_response, FIASController
from mks_backend.services.fias_entity.city_locality import CityLocalityService
from mks_backend.services.fias_entity.fias import get_addresses_from_response


@view_defaults(renderer='json')
class CityLocalityController:

    def __init__(self, request: Request):
        self.request = request
        self.service = CityLocalityService()
        self.fias_controller = FIASController(self.request)

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
        self.service.set_search_address(self.request.matchdict['text'])

        fias = self.fias_controller.get_fias_serialized()
        subject = fias.subject
        district = fias.district

        search_text = self.service.get_search_text(district, subject)
        addresses = get_addresses_from_response(get_fias_response(search_text))
        return self.service.get_cities_or_localities(addresses, district, subject)
