from mks_backend.repositories.meeting_repository import MeetingRepository

class MeetingService:

    def __init__(self):
        self.repository = MeetingRepository()

    def get_meetings_types(self) -> list:
        return self.repository.get_meetings_types()

    def get_meeting_fullname_by_id(self, id: int) -> str:
        return self.repository.get_meeting_fullname_by_id(id)
