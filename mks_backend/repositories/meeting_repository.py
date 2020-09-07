from mks_backend.models.meeting import MeetingsType
from mks_backend.repositories import DBSession


class MeetingRepository:

    def get_meetings_types(self) -> list:
        return DBSession.query(MeetingsType).all()

    @classmethod
    def get_meeting_fullname_by_id(cls, id: int) -> str:
        meeting = DBSession.query(MeetingsType).get(id)
        return meeting.fullname
