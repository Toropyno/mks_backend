from .model import CompletionDate
from .repository import CompletionDateRepository


class CompletionDateService:

    def __init__(self):
        self.repo = CompletionDateRepository()

    def add(self, completion_date: CompletionDate) -> None:
        self.repo.add(completion_date)

    def update(self, completion_date: CompletionDate) -> None:
        self.repo.update(completion_date)

    def get_all_completion_dates_by_contract_id(self, contract_id: int) -> list:
        return self.repo.get_all_completion_dates_by_contract_id(contract_id)

    def get_by_id(self, id: int) -> CompletionDate:
        return self.repo.get_by_id(id)

    def delete_by_id(self, id: int) -> None:
        self.repo.delete_by_id(id)
