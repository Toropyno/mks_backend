from mks_backend.models.meeting import Meeting
from mks_backend.repositories.meeting import MeetingRepository


class MeetingService:

    def __init__(self):
        self.repo = MeetingRepository()

    def get_all_meeting_types(self) -> list:
        return self.repo.get_all_meeting_types()

    def get_meeting_type_by_id(self, id: int) -> Meeting:
        return self.repo.get_meeting_type_by_id(id)

    def add_meeting_type(self, meeting_type: Meeting) -> None:
        self.repo.add_meeting_type(meeting_type)

    def update_meeting_type(self, new_meeting_type: Meeting) -> None:
        self.repo.update_meeting_type(new_meeting_type)

    def delete_meeting_type_by_id(self, id: int) -> None:
        self.repo.delete_meeting_type_by_id(id)
