from mks_backend.models.protocols.meeting import Meeting
from mks_backend.session import DBSession

from mks_backend.errors import DBBasicError


class MeetingRepository:

    def __init__(self):
        self._query = DBSession.query(Meeting)

    def get_meeting_type_by_id(self, id: int) -> Meeting:
        return self._query.get(id)

    def get_all_meeting_types(self) -> list:
        return self._query.all()

    def add_meeting_type(self, meeting_type: Meeting) -> None:
        DBSession.add(meeting_type)
        DBSession.commit()

    def delete_meeting_type_by_id(self, id: int) -> None:
        meeting_type = self.get_meeting_type_by_id(id)
        DBSession.delete(meeting_type)
        DBSession.commit()

    def update_meeting_type(self, meeting_type: Meeting) -> None:
        if DBSession.merge(meeting_type) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('meeting_type_ad')
