from .model import ReasonStopping

from mks_backend.session import DBSession
from mks_backend.errors import DBBasicError


class ReasonStoppingRepository:

    def __init__(self):
        self._query = DBSession.query(ReasonStopping)

    def get_all_reason_stoppings(self) -> list:
        return self._query.order_by(ReasonStopping.fullname).all()

    def add_reason_stopping(self, reason_stopping: ReasonStopping) -> None:
        DBSession.add(reason_stopping)
        DBSession.commit()

    def delete_reason_stopping_by_id(self, id: int) -> None:
        self._query.filter(ReasonStopping.reason_stopping_id == id).delete()
        DBSession.commit()

    def update_reason_stopping(self, new_reason_stopping: ReasonStopping) -> None:
        if DBSession.merge(new_reason_stopping) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('reason_stopping_ad')

    def get_reason_stopping_by_id(self, id: int) -> ReasonStopping:
        return self._query.get(id)
