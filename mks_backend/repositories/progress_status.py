from mks_backend.errors.db_basic_error import db_error_handler
from mks_backend.models.progress_status import ProgressStatus
from mks_backend.repositories import DBSession


class ProgressStatusRepository:

    def get_progress_status_by_id(self, id: int) -> ProgressStatus:
        return DBSession.query(ProgressStatus).get(id)

    def get_all_progress_statuses(self) -> list:
        return DBSession.query(ProgressStatus).all()

    @db_error_handler
    def add_progress_status(self, progress_status: ProgressStatus) -> None:
        DBSession.add(progress_status)
        DBSession.commit()

    def delete_progress_status_by_id(self, id: int) -> None:
        progress_status = self.get_progress_status_by_id(id)
        DBSession.delete(progress_status)
        DBSession.commit()

    @db_error_handler
    def update_progress_status(self, progress_status: ProgressStatus) -> None:
        DBSession.query(ProgressStatus).filter_by(progress_statuses_id=progress_status.progress_statuses_id).update(
            {
                'fullname': progress_status.fullname,
            }
        )
