from .model import Courts
from .repository import CourtsRepository


class CourtService:

    def __init__(self):
        self.repo = CourtsRepository()

    def get_all_courts(self) -> list:
        return self.repo.get_all_courts()

    def get_court_by_id(self, id_: int) -> Courts:
        return self.repo.get_court_by_id(id_)

    def add_court(self, court: Courts) -> None:
        self.repo.add_court(court)

    def update_court(self, new_court: Courts) -> None:
        self.repo.update_court(new_court)

    def delete_court_by_id(self, id_: int) -> None:
        self.repo.delete_court_by_id(id_)
