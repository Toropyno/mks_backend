from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import ParticipantStatusSchema
from .serializer import ParticipantStatusSerializer
from .service import ParticipantStatusService


@view_defaults(renderer='json')
class ParticipantStatusController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ParticipantStatusService()
        self.serializer = ParticipantStatusSerializer()
        self.schema = ParticipantStatusSchema()

    @view_config(route_name='get_all_participant_statuses')
    def get_all_participant_statuses(self):
        participant_statuses = self.service.get_all_participant_statuses()
        return self.serializer.convert_list_to_json(participant_statuses)

    @view_config(route_name='add_participant_status')
    def add_participant_status(self):
        participant_status_deserialized = self.schema.deserialize(self.request.json_body)
        participant_status = self.serializer.convert_schema_to_object(participant_status_deserialized)
        self.service.add_participant_status(participant_status)
        return {'id': participant_status.participant_statuses_id}

    @view_config(route_name='delete_participant_status')
    def delete_participant_status(self):
        id = self.get_id()
        self.service.delete_participant_status_by_id(id)
        return {'id': id}

    @view_config(route_name='edit_participant_status')
    def edit_participant_status(self):
        participant_status_deserialized = self.schema.deserialize(self.request.json_body)
        participant_status_deserialized['id'] = self.get_id()

        new_participant_status = self.serializer.convert_schema_to_object(participant_status_deserialized)
        self.service.update_participant_status(new_participant_status)
        return {'id': new_participant_status.participant_statuses_id}

    @view_config(route_name='get_participant_status')
    def get_participant_status(self):
        id = self.get_id()
        participant_status = self.service.get_participant_status_by_id(id)
        return self.serializer.convert_object_to_json(participant_status)

    def get_id(self):
        return int(self.request.matchdict['id'])
