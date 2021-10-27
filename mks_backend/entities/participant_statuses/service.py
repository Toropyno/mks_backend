from .model import Participant_Statuses
from .repository import ParticipantStatusesRepository


class ParticipantStatusesService:

    def __init__(self):
        self.repo = ParticipantStatusesRepository()

    def get_all_participant_statuses(self) -> list:
        return self.repo.get_all_participant_statuses()

    def get_participant_statuse_by_id(self, id: int) -> Participant_Statuses:
        return self.repo.get_participant_statuse_by_id(id)

    def add_participant_statuse(self, participant_statuse: Participant_Statuses) -> None:
        self.repo.add_participant_statuse(participant_statuse)

    def update_participant_statuse(self, new_participant_statuse: Participant_Statuses) -> None:
        self.repo.update_participant_statuse(new_participant_statuse)

    def delete_participant_statuse_by_id(self, id: int) -> None:
        self.repo.get_participant_statuse_by_id(id)
