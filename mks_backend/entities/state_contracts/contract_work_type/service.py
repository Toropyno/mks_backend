from .model import ContractWorkType
from .repository import ContractWorkTypeRepository


class ContractWorkTypeService:

    def __init__(self):
        self.repo = ContractWorkTypeRepository()

    def add(self, contract_w_t: ContractWorkType) -> None:
        self.repo.add(contract_w_t)

    def update(self, contract_w_t: ContractWorkType) -> None:
        self.repo.update(contract_w_t)

    def get_all(self) -> list:
        return self.repo.get_all()

    def get_by_id(self, id: int) -> ContractWorkType:
        return self.repo.get_by_id(id)

    def delete_by_id(self, id: int) -> None:
        self.repo.delete_by_id(id)
