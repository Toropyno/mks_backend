from mks_backend.models.progress_status import ProgressStatus
from mks_backend.repositories.progress_status import ProgressStatusRepository


class ProgressStatusService:

    def __init__(self):
        self.repo = ProgressStatusRepository()

    def get_all_progress_statuses(self) -> list:
        return self.repo.get_all_progress_statuses()

    def get_progress_status_by_id(self, id: int) -> ProgressStatus:
        return self.repo.get_progress_status_by_id(id)

    def add_progress_status(self, progress_status: ProgressStatus) -> None:
        self.repo.add_progress_status(progress_status)

    def update_progress_status(self, new_progress_status: ProgressStatus) -> None:
        self.repo.update_progress_status(new_progress_status)

    def delete_progress_status_by_id(self, id: int) -> None:
        self.repo.delete_progress_status_by_id(id)