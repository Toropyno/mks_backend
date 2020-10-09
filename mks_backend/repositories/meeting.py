from mks_backend.errors.db_basic_error import db_error_handler
from mks_backend.models.meeting import Meeting
from mks_backend.repositories import DBSession


class MeetingRepository:

    def get_meeting_type_by_id(self, id: int) -> Meeting:
        return DBSession.query(Meeting).get(id)

    def get_all_meeting_types(self) -> list:
        return DBSession.query(Meeting).all()

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
        DBSession.query(Meeting).filter_by(meetings_type_id=meeting_type.meetings_type_id).update(
            {
                'fullname': meeting_type.fullname,
            }
        )
        DBSession.commit()
