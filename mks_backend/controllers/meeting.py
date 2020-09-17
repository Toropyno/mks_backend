from pyramid.view import view_config
from pyramid.request import Request

from mks_backend.services.meeting import MeetingService
from mks_backend.serializers.meeting import MeetingSerializer


class MeetingController:

    def __init__(self, request: Request):
        self.request = request
        self.service = MeetingService()
        self.serializer = MeetingSerializer()

    @view_config(route_name='get_meetings', renderer='json')
    def get_meetings_types(self):
        meetings = self.service.get_meetings_types()
        return self.serializer.convert_list_to_json(meetings)
