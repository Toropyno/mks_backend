from sqlalchemy import desc
from typing import List

from .model import WorkTripFile
from mks_backend.session import DBSession

from mks_backend.errors.db_basic_error import DBBasicError


class WorkTripFilesRepository:

    def __init__(self):
        self._query = DBSession.query(WorkTripFile)

    def get_work_trip_file_by_id(self, id_: int) -> WorkTripFile:
        work_trip_file = self._query.get(id_)
        if not work_trip_file:
            raise DBBasicError('work_trip_file_nf')
        return work_trip_file

    def get_all_work_trip_files_by_work_trip_id(self, work_trip_id: int) -> list:
        return self._query.filter(WorkTripFile.work_trips_id == work_trip_id)\
            .order_by(desc(WorkTripFile.upload_date)).all()

    def add_work_trip_file(self, work_trip_files: List[WorkTripFile]) -> None:
        DBSession.add_all(work_trip_files)
        DBSession.commit()

    def delete_work_trip_file(self, id_: int) -> None:
        work_trip_file = self.get_work_trip_file_by_id(id_)
        DBSession.delete(work_trip_file)
        DBSession.commit()
