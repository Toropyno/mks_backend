from .model import ParticipantStatus

from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.errors import serialize_error_handler


class ParticipantStatusSerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, participant_status: ParticipantStatus) -> dict:
        return {
            'id': participant_status.participant_statuses_id,
            'fullName': participant_status.fullname,
        }

    def convert_schema_to_object(self, schema: dict) -> ParticipantStatus:
        participant_status = ParticipantStatus()

        participant_status.participant_statuses_id = schema.get('id')
        participant_status.fullname = schema.get('fullName')

        return participant_status
