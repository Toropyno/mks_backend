from mks_backend.models.state_contracts.contract import Contract
from mks_backend.repositories.state_contracts.contract import ContractRepository


class ContractService:

    def __init__(self):
        self.repo = ContractRepository()

    def get_all_contracts(self) -> list:
        return self.repo.get_all()

    def get_contract(self, id_: int) -> Contract:
        return self.repo.get_contract(id_)

    def add_contract(self, contract: Contract) -> None:
        self.repo.add_contract(contract)

    def update_contract(self, new_contract: Contract) -> None:
        self.repo.update_contract(new_contract)

    def delete_contract_by_id(self, id_: int) -> None:
        self.repo.delete_contract(id_)
