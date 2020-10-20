from pyramid.request import Request
from pyramid.view import view_defaults, view_config

from mks_backend.controllers.fias_entity.fias import FIASController
from mks_backend.repositories.fias_entity.api import get_fias_response
from mks_backend.services.fias_entity.district import DistrictService
from mks_backend.services.fias_entity.fias import get_addresses_from_response


@view_defaults(renderer='json')
class DistrictController:

    def __init__(self, request: Request):
        self.request = request
        self.service = DistrictService()
        self.fias_controller = FIASController(self.request)

    @view_config(route_name='get_districts')
    def get_districts(self):
        """
        Get districts: 'р-н ', 'район ', 'у '
        """
        self.service.search_district = self.request.matchdict['text']
        fias_post = self.fias_controller.get_fias_serialized()

        search_text = self.service.get_search_text(fias_post.subject)
        addresses = get_addresses_from_response(get_fias_response(search_text))
        return self.service.get_districts(addresses, fias_post.subject)
