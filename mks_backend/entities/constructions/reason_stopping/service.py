from .model import ReasonStopping
from .repository import ReasonStoppingRepository


class ReasonStoppingService:

    def __init__(self):
        self.repo = ReasonStoppingRepository()

    def get_all_reason_stoppings(self) -> list:
        return self.repo.get_all_reason_stoppings()

    def get_reason_stopping_by_id(self, id: int) -> ReasonStopping:
        return self.repo.get_reason_stopping_by_id(id)

    def add_reason_stopping(self, reason_stopping: ReasonStopping) -> None:
        self.repo.add_reason_stopping(reason_stopping)

    def update_reason_stopping(self, new_reason_stopping: ReasonStopping) -> None:
        self.repo.update_reason_stopping(new_reason_stopping)

    def delete_reason_stopping_by_id(self, id: int) -> None:
        self.repo.delete_reason_stopping_by_id(id)
