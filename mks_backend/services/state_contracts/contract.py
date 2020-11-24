from mks_backend.models.state_contracts import Contract
from mks_backend.repositories.state_contracts import ContractRepository


class ContractService:

    def __init__(self):
        self.repo = ContractRepository()

    def get_all_by_construction_id(self, construction_id: int) -> list:
        return self.repo.get_all_by_construction_id(construction_id)

    def get_contract(self, id_: int) -> Contract:
        return self.repo.get_contract(id_)

    def add_contract(self, contract: Contract) -> None:
        self.repo.add_contract(contract)

    def edit_contract(self, contract: Contract) -> None:
        self.repo.edit_contract(contract)

    def delete_contract(self, id_: int) -> None:
        self.repo.delete_contract(id_)
