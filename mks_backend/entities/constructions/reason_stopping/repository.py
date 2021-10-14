from .model import ReasonStopping

from mks_backend.session import DBSession


class ReasonStoppingRepository:

    def __init__(self):
        self._query = DBSession.query(ReasonStopping)

    def get_all_reason_stoppings(self) -> list:
        return self._query.all()

    def add_reason_stopping(self, reason_stopping: ReasonStopping) -> None:
        DBSession.add(reason_stopping)
        DBSession.commit()

    def delete_reason_stopping_by_id(self, id: int) -> None:
        self._query.filter(ReasonStopping.reason_stopping_id == id).delete()
        DBSession.commit()

    def update_reason_stopping(self, new_reason_stopping: ReasonStopping) -> None:
        old_reason_stopping = self._query.filter_by(reason_stopping_id=new_reason_stopping.reason_stopping_id)
        old_reason_stopping.update(
            {
                'fullname': new_reason_stopping.fullname,
            }
        )
        DBSession.commit()

    def get_reason_stopping_by_id(self, id: int) -> ReasonStopping:
        return self._query.get(id)
