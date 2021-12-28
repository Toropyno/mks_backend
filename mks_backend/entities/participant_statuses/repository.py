from .model import ParticipantStatus
from mks_backend.session import DBSession
from mks_backend.errors import DBBasicError


class ParticipantStatusRepository:

    def __init__(self):
        self._query = DBSession.query(ParticipantStatus)

    def get_all_participant_statuses(self) -> list:
        return self._query.order_by(ParticipantStatus.fullname).all()

    def add_participant_status(self, participant_status: ParticipantStatus) -> None:
        DBSession.add(participant_status)
        DBSession.commit()

    def delete_participant_status_by_id(self, id: int) -> None:
        self._query.filter(ParticipantStatus.participant_statuses_id == id).delete()
        DBSession.commit()

    def update_participant_status(self, new_participant_status: ParticipantStatus) -> None:
        if DBSession.merge(new_participant_status) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('participant_status_ad')

    def get_participant_status_by_id(self, id: int):
        participant_status = self._query.get(id)
        if not participant_status:
            raise DBBasicError('participant_status_nf')
        return participant_status