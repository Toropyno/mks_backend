from mks_backend.models.state_contracts import Contract
from mks_backend.models import DBSession

from mks_backend.errors import db_error_handler, DBBasicError


class ContractRepository:

    def __init__(self):
        self._query = DBSession.query(Contract)

    def get_all_by_construction_id(self, construction_id: int) -> list:
        return self._query.filter(Contract.construction_id == construction_id).order_by(Contract.contract_date).all()

    def get_contract(self, id_: int) -> Contract:
        contract = self._query.get(id_)
        if not contract:
            raise DBBasicError('contract_nf')
        else:
            return contract

    @db_error_handler
    def add_contract(self, contract: Contract) -> None:
        DBSession.add(contract)
        DBSession.commit()

    @db_error_handler
    def edit_contract(self, contract: Contract) -> None:
        DBSession.merge(contract)
        DBSession.commit()

    def delete_contract(self, id_: int) -> None:
        self._query.filter(Contract.contracts_id == id_).delete()
        DBSession.commit()
