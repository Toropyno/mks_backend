from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import MeetingSchema
from .serializer import MeetingSerializer
from .service import MeetingService


@view_defaults(renderer='json')
class MeetingController:

    def __init__(self, request: Request):
        self.request = request
        self.service = MeetingService()
        self.serializer = MeetingSerializer()
        self.schema = MeetingSchema()

    @view_config(route_name='get_all_meeting_types')
    def get_all_meeting_types(self):
        meeting_types = self.service.get_all_meeting_types()
        return self.serializer.convert_list_to_json(meeting_types)

    @view_config(route_name='add_meeting_type')
    def add_meeting_type(self):
        meeting_type_deserialized = self.schema.deserialize(self.request.json_body)
        meeting_type = self.serializer.convert_schema_to_object(meeting_type_deserialized)
        self.service.add_meeting_type(meeting_type)
        return {'id': meeting_type.meetings_type_id}

    @view_config(route_name='delete_meeting_type')
    def delete_meeting_type(self):
        id = self.request.matchdict['id']
        self.service.delete_meeting_type_by_id(id)
        return {'id': id}

    @view_config(route_name='edit_meeting_type')
    def edit_meeting_type(self):
        id = self.request.matchdict['id']
        meeting_type_deserialized = self.schema.deserialize(self.request.json_body)
        meeting_type_deserialized['id'] = id
        new_meeting_type = self.serializer.convert_schema_to_object(meeting_type_deserialized)
        self.service.update_meeting_type(new_meeting_type)
        return {'id': id}

    @view_config(route_name='get_meeting_type')
    def get_meeting_type(self):
        id = self.request.matchdict['id']
        meeting_type = self.service.get_meeting_type_by_id(id)
        return self.serializer.to_json(meeting_type)
