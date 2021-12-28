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

    def get_by_id(self, id_: int) -> ContractWorkType:
        return self.repo.get_by_id(id_)

    def delete_by_id(self, id_: int) -> None:
        self.repo.delete_by_id(id_)
