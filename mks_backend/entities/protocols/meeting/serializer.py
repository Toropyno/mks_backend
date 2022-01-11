from .model import Meeting

from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.errors import serialize_error_handler


class MeetingSerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, meeting: Meeting) -> dict:
        return {
            'id': meeting.meetings_type_id,
            'fullName': meeting.fullname,
        }

    def to_mapped_object(self, schema: dict) -> Meeting:
        meeting_type = Meeting()

        meeting_type.meetings_type_id = schema.get('id')
        meeting_type.fullname = schema.get('fullName')

        return meeting_type
