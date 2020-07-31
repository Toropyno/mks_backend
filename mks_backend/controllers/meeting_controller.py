from pyramid.view import view_config, view_defaults

from mks_backend.repositories.meeting_repository import MeetingRepository


class ProtocolController(object):
    def __init__(self, request):
        self.request = request
        self.repository = MeetingRepository()
        # self.serializer = ProtocolSerializer()
        # self.service = ProtocolService()

    @view_config(route_name='add_protocol', request_method='GET', renderer='json')
    def get_meetings_types(self):
        return self.repository.get_meetings_types()