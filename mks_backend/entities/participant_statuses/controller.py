from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import ParticipantStatusesSchema
from .serializer import ParticipantStatusesSerializer
from .service import ParticipantStatusesService


@view_defaults(renderer='json')
class ParticipantStatusesController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ParticipantStatusesService()
        self.serializer = ParticipantStatusesSerializer()
        self.schema = ParticipantStatusesSchema()

    @view_config(route_name='get_all_participant_statuses')
    def get_all_participant_statuses(self):
        participant_statuses = self.service.get_all_participant_statuses()
        return self.serializer.convert_list_to_json(participant_statuses)

    @view_config(route_name='add_participant_statuse')
    def add_court(self):
        participant_statuse_deserialized = self.schema.deserialize(self.request.json_body)
        participant_statuse = self.serializer.convert_schema_to_object(participant_statuse_deserialized)
        self.service.add_participant_statuse(participant_statuse)
        return {'id': participant_statuse.participant_statuses_id}

    @view_config(route_name='delete_participant_statuse')
    def delete_participant_statuse(self):
        id = self.get_id()
        self.service.delete_participant_statuse_by_id(id)
        return {'id': id}

    @view_config(route_name='edit_participant_statuse')
    def edit_participant_statuse(self):
        participant_statuse_deserialized = self.schema.deserialize(self.request.json_body)
        participant_statuse_deserialized['id'] = self.get_id()

        new_participant_statuse = self.serializer.convert_schema_to_object(participant_statuse_deserialized)
        self.service.update_participant_statuse(new_participant_statuse)
        return {'id': new_participant_statuse.participant_statuses_id}

    @view_config(route_name='get_participant_statuse')
    def get_court(self):
        id = self.get_id()
        participant_statuse = self.service.get_participant_statuse_by_id(id)
        return self.serializer.convert_object_to_json(participant_statuse)

    def get_id(self):
        return int(self.request.matchdict['id'])
