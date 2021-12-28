from .model import ParticipantStatus
from .repository import ParticipantStatusRepository


class ParticipantStatusService:

    def __init__(self):
        self.repo = ParticipantStatusRepository()

    def get_all_participant_statuses(self) -> list:
        return self.repo.get_all_participant_statuses()

    def get_participant_status_by_id(self, id_: int) -> ParticipantStatus:
        return self.repo.get_participant_status_by_id(id_)

    def add_participant_status(self, participant_status: ParticipantStatus) -> None:
        self.repo.add_participant_status(participant_status)

    def update_participant_status(self, new_participant_status: ParticipantStatus) -> None:
        self.repo.update_participant_status(new_participant_status)

    def delete_participant_status_by_id(self, id_: int) -> None:
        self.repo.get_participant_status_by_id(id_)
