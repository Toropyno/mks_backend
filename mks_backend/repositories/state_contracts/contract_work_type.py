from mks_backend.models.state_contracts.contract_work_type import ContractWorkType
from mks_backend.repositories import DBSession

from mks_backend.errors.db_basic_error import db_error_handler


class ContractWorkTypeRepository:

    def __init__(self):
        self._query = DBSession.query(ContractWorkType)

    @db_error_handler
    def add(self, contract_w_t: ContractWorkType) -> None:
        DBSession.add(contract_w_t)
        DBSession.commit()

    def get_by_id(self, id: int) -> ContractWorkType:
        return self._query.get(id)

    def get_all(self) -> list:
        return self._query.order_by(ContractWorkType.fullname).all()

    def delete_by_id(self, id: int) -> None:
        contract_w_t = self.get_by_id(id)
        DBSession.delete(contract_w_t)
        DBSession.commit()

    @db_error_handler
    def update(self, contract_w_t: ContractWorkType) -> None:
        self._query.filter_by(contract_worktypes_id=contract_w_t.contract_worktypes_id).update(
            {
                'fullname': contract_w_t.fullname,
            }
        )
        DBSession.commit()
