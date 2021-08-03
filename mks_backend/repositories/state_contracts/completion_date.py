from mks_backend.session import DBSession
from mks_backend.models.state_contracts.completion_date import CompletionDate

from mks_backend.errors.db_basic_error import DBBasicError


class CompletionDateRepository:

    def __init__(self):
        self._query = DBSession.query(CompletionDate)

    def add(self, completion_date: CompletionDate) -> None:
        DBSession.add(completion_date)
        DBSession.commit()

    def get_by_id(self, id: int) -> CompletionDate:
        completion_date = self._query.get(id)
        if not completion_date:
            raise DBBasicError('completion_date_nf')
        return completion_date

    def get_all_completion_dates_by_contract_id(self, contract_id: int) -> list:
        return self._query.filter(CompletionDate.contracts_id == contract_id).order_by(CompletionDate.end_date).all()

    def delete_by_id(self, id: int) -> None:
        completion_date = self.get_by_id(id)
        DBSession.delete(completion_date)
        DBSession.commit()

    def update(self, completion_date: CompletionDate) -> None:
        self._query.filter_by(completion_dates_id=completion_date.completion_dates_id).update(
            {
                'contracts_id': completion_date.contracts_id,
                'contract_worktypes_id': completion_date.contract_worktypes_id,
                'end_date': completion_date.end_date,
            }
        )
        DBSession.commit()
