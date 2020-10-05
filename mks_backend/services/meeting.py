from mks_backend.repositories.meeting import MeetingRepository


class MeetingService:

    def __init__(self):
        self.repository = MeetingRepository()

    def get_meetings_types(self) -> list:
        return self.repository.get_meetings_types()
