from mks_backend.models.meeting import MeetingsType
from mks_backend.repositories import DBSession


class MeetingRepository(object):

    def get_meetings_types(self):
        meetings_query = DBSession.query(MeetingsType).all()
        return [{'id': meeting.meetings_type_id, 'fullName': meeting.fullname} for meeting in meetings_query]

    @classmethod
    def get_meeting_fullname_by_id(cls, id):
        meeting = DBSession.query(MeetingsType).get(id)
        return meeting.fullname
