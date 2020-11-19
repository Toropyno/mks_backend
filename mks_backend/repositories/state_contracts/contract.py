from mks_backend.errors.db_basic_error import db_error_handler
from mks_backend.models.state_contracts.contract import Contract
from mks_backend.repositories import DBSession


class ContractRepository:

    def __init__(self):
        self._query = DBSession(Contract)

    def get_all(self) -> list:
        return self._query.order_by(Contract.contract_date).all()

    def get_contract(self, id_: int) -> Contract:
        return self._query.get(id_)

    @db_error_handler
    def add_contract(self, contract: Contract) -> None:
        DBSession.add(contract)
        DBSession.commit()

    @db_error_handler
    def update_contract(self, contract: Contract) -> None:
        self._query.filter(Contract.contracts_id == contract.contracts_id).update(
            {
                'contract_date': contract.contract_date,
            }
        )
        DBSession.commit()

    def delete_contract(self, id_: int) -> None:
        self._query.filter(Contract.contracts_id == id_).delete()
        DBSession.commit()
