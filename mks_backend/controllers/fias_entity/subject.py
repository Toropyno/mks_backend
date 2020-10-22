from pyramid.request import Request
from pyramid.view import view_defaults, view_config

from mks_backend.services.fias_entity.subject import SubjectService


@view_defaults(renderer='json')
class SubjectController:

    def __init__(self, request: Request):
        self.request = request
        self.service = SubjectService()

    @view_config(route_name='get_subjects')
    def get_subjects(self):
        """
        subjects: 'обл. ', 'обл ', 'Респ. ', 'Респ ', 'край '
        """
        self.service.search_subject = self.request.matchdict['text']
        return self.service.get_subjects()
