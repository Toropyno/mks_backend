from typing import Tuple

from sqlalchemy import and_

from mks_backend.session import DBSession

from .model import LitigationSubject


class LitigationSubjectRepository:

    def __init__(self):
        self._query = DBSession.query(LitigationSubject)

    def delete_litigation_subject(self, litigation_id: int, construction_id: int) -> None:
        self._query.filter(
            and_(LitigationSubject.litigation_id == litigation_id, LitigationSubject.construction_id == construction_id)
        ).delete()
        DBSession.commit()

    def add_litigation_subjects(self, litigation_subjects: Tuple[LitigationSubject]) -> None:
        for litigation_subject in litigation_subjects:
            DBSession.merge(litigation_subject)
        DBSession.commit()
