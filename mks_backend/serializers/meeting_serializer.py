from mks_backend.models.meeting import MeetingsType


class MeetingSerializer:

    @classmethod
    def convert_object_to_json(cls, meeting: MeetingsType) -> dict:
        return {
            'id': meeting.meetings_type_id,
            'fullName': meeting.fullname,
        }

    def convert_list_to_json(self, meetings: list) -> list:
        return list(map(self.convert_object_to_json, meetings))
