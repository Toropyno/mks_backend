from pyramid.request import Request
from pyramid.view import view_defaults, view_config

from mks_backend.controllers.fias_entity.fias import get_fias_response
from mks_backend.services.fias_entity.fias import get_addresses_from_responce
from mks_backend.services.fias_entity.subject import SubjectService


@view_defaults(renderer='json')
class SubjectController:

    def __init__(self, request: Request):
        self.request = request
        self.service = SubjectService()

    @view_config(route_name='get_subjects')
    def get_subjects(self):
        """
        Get subject: 'обл. ', 'обл', 'Респ. ', 'Респ', 'край '
        """
        text = self.request.matchdict['text']
        self.service.set_text(text)

        addresses = get_addresses_from_responce(get_fias_response(text))
        return self.service.get_subjects(addresses)
