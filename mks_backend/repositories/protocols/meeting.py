from mks_backend.models.protocols.meeting import Meeting
from mks_backend.models import DBSession

from mks_backend.errors.db_basic_error import db_error_handler


class MeetingRepository:

    def __init__(self):
        self._query = DBSession.query(Meeting)

    def get_meeting_type_by_id(self, id: int) -> Meeting:
        return self._query.get(id)

    def get_all_meeting_types(self) -> list:
        return self._query.all()

    @db_error_handler
    def add_meeting_type(self, meeting_type: Meeting) -> None:
        DBSession.add(meeting_type)
        DBSession.commit()

    def delete_meeting_type_by_id(self, id: int) -> None:
        meeting_type = self.get_meeting_type_by_id(id)
        DBSession.delete(meeting_type)
        DBSession.commit()

    @db_error_handler
    def update_meeting_type(self, meeting_type: Meeting) -> None:
        DBSession.merge(meeting_type)
        DBSession.commit()
