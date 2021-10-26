from .model import CourtDecision
from .repository import CourtDecisionRepository


class CourtDecisionService:

    def __init__(self):
        self.repo = CourtDecisionRepository()

    def get_all_court_decisions(self) -> list:
        return self.repo.get_all_court_decisions()

    def get_court_decision_by_id(self, id: int) -> CourtDecision:
        return self.repo.get_court_decision_by_id(id)

    def add_court_decision(self, court_decision: CourtDecision) -> None:
        self.repo.add_court_decision(court_decision)

    def update_court_decision(self, new_court_decision: CourtDecision) -> None:
        self.repo.update_court_decision(new_court_decision)

    def delete_court_decision_by_id(self, id: int) -> None:
        self.repo.delete_court_decision_by_id(id)
