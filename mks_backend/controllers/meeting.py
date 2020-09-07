from pyramid.view import view_config
from pyramid.request import Request

from mks_backend.repositories.meeting import MeetingRepository


class MeetingController:

    def __init__(self, request: Request):
        self.request = request
        self.repository = MeetingRepository()

    @view_config(route_name='add_protocol', request_method='GET', renderer='json')
    def get_meetings_types(self) -> list:
        return self.repository.get_meetings_types()
