from mks_backend.errors import DBBasicError
from mks_backend.session import DBSession

from .model import CourtDecision


class CourtDecisionRepository:

    def __init__(self):
        self._query = DBSession.query(CourtDecision)

    def get_all_court_decisions(self) -> list:
        return self._query.order_by(CourtDecision.fullname).all()

    def add_court_decision(self, court_decision: CourtDecision) -> None:
        DBSession.add(court_decision)
        DBSession.commit()

    def delete_court_decision_by_id(self, id: int) -> None:
        self._query.filter(CourtDecision.court_decisions_id == id).delete()
        DBSession.commit()

    def update_court_decision(self, new_court_decision):
        if DBSession.merge(new_court_decision) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('court_decision_ad')

    def get_court_decision_by_id(self, id_: int):
        court = self._query.get(id_)
        if not court:
            raise DBBasicError('court_decision_nf')
        return court
