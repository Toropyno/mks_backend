from pyramid.request import Request
from pyramid.view import view_defaults, view_config

from mks_backend.services.fias_entity.fias import FIASService
from mks_backend.services.fias_entity.subject import SubjectService


@view_defaults(renderer='json')
class SubjectController:

    def __init__(self, request: Request):
        self.request = request
        self.service = SubjectService()
        self.service_FIAS = FIASService()

    @view_config(route_name='get_subjects')
    def get_subjects(self):
        """
        Get subjects: 'обл. ', 'обл ', 'Респ. ', 'Респ ', 'край '
        """
        search_subject = self.request.matchdict['text']
        self.service.search_subject = search_subject

        addresses = self.service_FIAS.get_addresses_from_response(self.service_FIAS.get_fias_response(search_subject))
        return self.service.get_subjects(addresses)
