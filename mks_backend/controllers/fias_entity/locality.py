from pyramid.request import Request
from pyramid.view import view_defaults, view_config

from mks_backend.controllers.fias_entity.city import CityController
from mks_backend.services.fias_entity.city import CityOrLocalityService
from mks_backend.services.fias_entity.locality import LocalityService


@view_defaults(renderer='json')
class LocalityController:

    def __init__(self, request: Request):
        self.request = request
        self.service = LocalityService()
        self.service = CityOrLocalityService()

    @view_config(route_name='get_localities')
    def get_localities(self):
        """
              Get locality: 'пгт. ', 'п. ', 'д.', 'с. ', 'п. им.'
        """
        self.service.set_city_or_locality(['пгт. ', 'п. ', 'д.', 'с. ', 'п. им.'])
        localities = self.get_city_or_locality()
        return localities
