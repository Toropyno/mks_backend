from mks_backend.errors import DBBasicError
from mks_backend.session import DBSession

from .model import ContractWorkType


class ContractWorkTypeRepository:

    def __init__(self):
        self._query = DBSession.query(ContractWorkType)

    def add(self, contract_w_t: ContractWorkType) -> None:
        DBSession.add(contract_w_t)
        DBSession.commit()

    def get_by_id(self, id_: int) -> ContractWorkType:
        contract_w_t = self._query.get(id_)
        if not contract_w_t:
            raise DBBasicError('contract_work_type_nf')
        return contract_w_t

    def get_all(self) -> list:
        return self._query.order_by(ContractWorkType.fullname).all()

    def delete_by_id(self, id_: int) -> None:
        contract_w_t = self.get_by_id(id_)
        DBSession.delete(contract_w_t)
        DBSession.commit()

    def update(self, contract_w_t: ContractWorkType) -> None:
        self._query.filter_by(contract_worktypes_id=contract_w_t.contract_worktypes_id).update(
            {
                'fullname': contract_w_t.fullname,
            }
        )
        DBSession.commit()
