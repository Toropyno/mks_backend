from mks_backend.models.meeting import Meeting
from mks_backend.repositories import DBSession


class MeetingRepository:

    def get_meetings_types(self) -> list:
        meetings_query = DBSession.query(Meeting).all()
        return [{'id': meeting.meetings_type_id, 'fullName': meeting.fullname} for meeting in meetings_query]

    @classmethod
    def get_meeting_fullname_by_id(cls, id: int) -> str:
        meeting = DBSession.query(Meeting).get(id)
        return meeting.fullname
