from mks_backend.models.meeting import Meeting


class MeetingSerializer:

    def convert_object_to_json(self, meeting: Meeting) -> dict:
        return {
            'id': meeting.meetings_type_id,
            'fullName': meeting.fullname,
        }

    def convert_list_to_json(self, meetings: list) -> list:
        return list(map(self.convert_object_to_json, meetings))
