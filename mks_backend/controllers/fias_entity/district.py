from pyramid.request import Request
from pyramid.view import view_defaults, view_config

from mks_backend.controllers.fias_entity.fias import FIASController
from mks_backend.services.fias_entity.district import DistrictService
from mks_backend.services.fias_entity.fias import FIASService


@view_defaults(renderer='json')
class DistrictController:

    def __init__(self, request: Request):
        self.request = request
        self.service = DistrictService()
        self.controller_FIAS = FIASController(self.request)
        self.service_FIAS = FIASService()

    @view_config(route_name='get_districts')
    def get_districts(self):
        """
        districts: 'р-н ', 'район ', 'у '
        """
        self.service.search_district = self.request.matchdict['text']
        fias_post = self.controller_FIAS.get_fias_serialized()
        return self.service.get_districts(fias_post.subject)
