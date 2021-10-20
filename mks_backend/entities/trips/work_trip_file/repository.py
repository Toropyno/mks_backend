from sqlalchemy import desc

from .model import WorkTripFiles
from mks_backend.session import DBSession

from mks_backend.errors.db_basic_error import DBBasicError


class WorkTripFilesRepository:

    def __init__(self):
        self._query = DBSession.query(WorkTripFiles)

    def get_work_trip_file_by_id(self, id_: int) -> WorkTripFiles:
        work_trip_file = self._query.get(id_)
        if not work_trip_file:
            raise DBBasicError('work_trip_file_nf')
        return work_trip_file

    def get_all_work_trip_files(self, work_trip_id: int) -> list:
        return self._query.filter(WorkTripFiles.work_trips_id == work_trip_id)\
            .order_by(desc(WorkTripFiles.upload_date)).all()

    def add_work_trip_file(self, work_trip_file: WorkTripFiles) -> None:
        DBSession.add(work_trip_file)
        DBSession.commit()

    def delete_work_trip_file(self, id_: int) -> None:
        work_trip_file = self.get_work_trip_file_by_id(id_)
        if not work_trip_file:
            raise DBBasicError('work_trip_file_nf')
        DBSession.delete(work_trip_file)
        DBSession.commit()
