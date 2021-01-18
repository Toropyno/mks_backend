from mks_backend.models.state_contracts.contract_status import ContractStatus

from mks_backend.session import DBSession


class ContractStatusRepository:

    def __init__(self):
        self._query = DBSession.query(ContractStatus)

    def get_all_contract_statuses(self) -> list:
        return self._query.all()

    def add_contract_status(self, contract_status: ContractStatus) -> None:
        DBSession.add(contract_status)
        DBSession.commit()

    def delete_contract_status_by_id(self, id: int) -> None:
        self._query.filter(ContractStatus.contract_statuses_id == id).delete()
        DBSession.commit()

    def update_contract_status(self, new_contract_status: ContractStatus) -> None:
        old_contract_status = self._query.filter_by(contract_statuses_id=new_contract_status.contract_statuses_id)
        old_contract_status.update(
            {
                'fullName': new_contract_status.fullname,
            }
        )
        DBSession.commit()

    def get_contract_status_by_id(self, id: int) -> ContractStatus:
        return self._query.get(id)
