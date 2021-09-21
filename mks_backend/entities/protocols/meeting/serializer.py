from .model import Meeting

from mks_backend.errors import serialize_error_handler


class MeetingSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, meeting: Meeting) -> dict:
        return {
            'id': meeting.meetings_type_id,
            'fullName': meeting.fullname,
        }

    def convert_list_to_json(self, meetings: list) -> list:
        return list(map(self.convert_object_to_json, meetings))

    def convert_schema_to_object(self, schema: dict) -> Meeting:
        meeting_type = Meeting()

        meeting_type.meetings_type_id = schema.get('id')
        meeting_type.fullname = schema.get('fullName')

        return meeting_type
