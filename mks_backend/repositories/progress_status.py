from mks_backend.models.progress_status import ProgressStatus
from mks_backend.models import DBSession

from mks_backend.errors.db_basic_error import db_error_handler


class ProgressStatusRepository:

    def __init__(self):
        self._query = DBSession.query(ProgressStatus)

    def get_progress_status_by_id(self, id: int) -> ProgressStatus:
        return self._query.get(id)

    def get_all_progress_statuses(self) -> list:
        return self._query.order_by(ProgressStatus.fullname).all()

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
        DBSession.merge(progress_status)
        DBSession.commit()
