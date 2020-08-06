from mks_backend.models.meeting import Meetings_type
from mks_backend.repositories import DBSession


class MeetingRepository(object):
    def get_meetings_types(self):
        meetings_query = DBSession.query(Meetings_type).all()
        return [{'id': meeting.meetings_type_id, 'fullName': meeting.fullname} for meeting in meetings_query]

    @classmethod
    def get_meeting_fullname_by_id(cls, id):
        meeting = DBSession.query(Meetings_type).get(id)
        return meeting.fullname
