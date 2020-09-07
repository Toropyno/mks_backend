from pyramid.view import view_config
from pyramid.request import Request

from mks_backend.services.meeting_service import MeetingService
from mks_backend.serializers.meeting_serializer import MeetingSerializer


class MeetingController:

    def __init__(self, request: Request):
        self.request = request
        self.service = MeetingService()
        self.serializer = MeetingSerializer()

    @view_config(route_name='add_protocol', request_method='GET', renderer='json')
    def get_meetings_types(self):
        meetings = self.service.get_meetings_types()
        return self.serializer.convert_list_to_json(meetings)
