from .model import Contract
from mks_backend.session import DBSession

from mks_backend.errors import DBBasicError


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

    def add_contract(self, contract: Contract) -> None:
        DBSession.add(contract)
        DBSession.commit()

    def edit_contract(self, contract: Contract) -> None:
        if DBSession.merge(contract) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('contract_ad')

    def delete_contract(self, id_: int) -> None:
        self._query.filter(Contract.contracts_id == id_).delete()
        DBSession.commit()
