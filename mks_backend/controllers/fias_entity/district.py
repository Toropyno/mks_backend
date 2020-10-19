from pyramid.request import Request
from pyramid.view import view_defaults, view_config

from mks_backend.controllers.fias_entity.fias import get_fias_response, FIASController
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
        Get district: 'р-н ', 'район ', ' у '
        """
        text = self.request.matchdict['text']
        self.service.set_text(text)
        search_text = text

        fias = self.fias_controller.get_fias_serialized()
        subject = fias.subject
        # subject = None

        if subject is not None:
            search_text = subject + ', ' + search_text
        addresses = get_addresses_from_response(get_fias_response(search_text))

        return self.service.get_districts(addresses, subject)
