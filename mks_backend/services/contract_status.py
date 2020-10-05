from mks_backend.models.contract_status import ContractStatus
from mks_backend.repositories.contract_status import ContractStatusRepository


class ContractStatusService:

    def __init__(self):
        self.repo = ContractStatusRepository()

    def get_all_contract_statuses(self) -> list:
        return self.repo.get_all_contract_statuses()

    def get_contract_status_by_id(self, id: int) -> ContractStatus:
        return self.repo.get_contract_status_by_id(id)

    def add_contract_status(self, contract_status: ContractStatus) -> None:
        self.repo.add_contract_status(contract_status)

    def update_contract_status(self, new_contract_status: ContractStatus) -> None:
        self.repo.update_contract_status(new_contract_status)

    def delete_contract_status_by_id(self, id: int) -> None:
        self.repo.delete_contract_status_by_id(id)
