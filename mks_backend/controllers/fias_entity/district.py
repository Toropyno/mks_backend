from pyramid.request import Request
from pyramid.view import view_defaults, view_config

from mks_backend.controllers.fias_entity.fias import FIASController
from mks_backend.services.fias_entity.district import DistrictService


@view_defaults(renderer='json')
class DistrictController:

    def __init__(self, request: Request):
        self.request = request
        self.service = DistrictService()
        self.controller_FIAS = FIASController(self.request)

    @view_config(route_name='districts_hints')
    def districts_hints(self):
        """
        districts: 'р-н ', 'район ', 'у '
        """
        self.service.search_district = self.request.matchdict['text']
        fias_post = self.controller_FIAS.get_fias_serialized()
        return self.service.get_districts(fias_post.subject)
