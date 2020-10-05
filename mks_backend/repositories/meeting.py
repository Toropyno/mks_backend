from mks_backend.models.meeting import Meeting
from mks_backend.repositories import DBSession


class MeetingRepository:

    def get_meetings_types(self) -> list:
        return DBSession.query(Meeting).all()
