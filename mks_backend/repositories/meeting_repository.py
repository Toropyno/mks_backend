from mks_backend.models.meeting import Meeting
from mks_backend.repositories import DBSession


class MeetingRepository(object):

    def get_meetings_types(self):
        meetings_query = DBSession.query(Meeting).all()
        return [meeting.meetings_type_id for meeting in meetings_query]
