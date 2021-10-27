from .model import Participant_Statuses
from mks_backend.session import DBSession


from mks_backend.errors import DBBasicError


class ParticipantStatusesRepository:

    def __init__(self):
        self._query = DBSession.query(Participant_Statuses)

    def get_all_participant_statuses(self) -> list:
        return self._query.order_by(Participant_Statuses.fullname).all()

    def add_participant_statuse(self, participant_statuse: Participant_Statuses) -> None:
        DBSession.add(participant_statuse)
        DBSession.commit()

    def delete_participant_statuse_by_id(self, id: int) -> None:
        self._query.filter(Participant_Statuses.participant_statuses_id == id).delete()
        DBSession.commit()

    def update_participant_statuse(self, new_participant_statuse: Participant_Statuses) -> None:
        if DBSession.merge(new_participant_statuse) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('participant_statuse_ad')

    def get_participant_statuse_by_id(self, id: int):
        participant_statuse = self._query.get(id)
        if not participant_statuse:
            raise DBBasicError('participant_statuse_nf')
        return participant_statuse
