from mks_backend.errors import DBBasicError
from mks_backend.session import DBSession

from .model import ProgressStatus


class ProgressStatusRepository:

    def __init__(self):
        self._query = DBSession.query(ProgressStatus)

    def get_progress_status_by_id(self, id_: int) -> ProgressStatus:
        return self._query.get(id_)

    def get_all_progress_statuses(self) -> list:
        return self._query.order_by(ProgressStatus.fullname).all()

    def add_progress_status(self, progress_status: ProgressStatus) -> None:
        DBSession.add(progress_status)
        DBSession.commit()

    def delete_progress_status_by_id(self, id_: int) -> None:
        progress_status = self.get_progress_status_by_id(id_)
        DBSession.delete(progress_status)
        DBSession.commit()

    def update_progress_status(self, progress_status: ProgressStatus) -> None:
        if DBSession.merge(progress_status) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('progress_status_ad')
