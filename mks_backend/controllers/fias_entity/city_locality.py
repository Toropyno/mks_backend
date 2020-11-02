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

    @view_config(route_name='create_cities_hints')
    def create_cities_hints(self):
        """
            Находит подсказки для города РФ.
            К cities относятся: 'г. ', 'г ', 'город '
        """
        self.service.set_sity_socr_names()
        return self.create_cities_or_localities_hints()

    @view_config(route_name='create_localities_hints')
    def create_localities_hints(self):
        """
            Находит подсказки для поселения РФ.
            К localities относятся: 'пгт. ', 'пгт ', 'п. ', 'п ', 'д. ', 'д ', 'с. ', 'с ', 'п. им. ', 'п им ', 'ст-ца ',
                                    'х ', 'х. ', 'рп ', 'рп. '
        """
        self.service.set_locality_socr_names()
        return self.create_cities_or_localities_hints()

    def create_cities_or_localities_hints(self) -> list:
        self.service.search_address = self.request.matchdict['text']
        fias_post = self.controller_FIAS.get_fias_serialized()
        return list(self.service.create_cities_or_localities_hints(fias_post))
