from mks_backend.models.meeting import Meeting

from mks_backend.errors.serilize_error import serialize_error_handler


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
