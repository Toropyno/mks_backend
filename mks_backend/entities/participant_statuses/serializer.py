from .model import Participant_Statuses

from mks_backend.errors import serialize_error_handler


class ParticipantStatusesSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, participant_statuses: Participant_Statuses) -> dict:
        return {
            'id': participant_statuses.participant_statuses_id,
            'fullName': participant_statuses.fullname,
        }

    def convert_list_to_json(self, participant_statuses: list) -> list:
        return list(map(self.convert_object_to_json, participant_statuses))

    def convert_schema_to_object(self, schema: dict) -> Participant_Statuses:
        participant_statuses = Participant_Statuses()

        participant_statuses.participant_statuses_id = schema.get('id')
        participant_statuses.fullname = schema.get('fullName')

        return participant_statuses
