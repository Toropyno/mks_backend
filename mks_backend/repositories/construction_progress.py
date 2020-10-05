from sqlalchemy import desc

from mks_backend.errors.db_basic_error import db_error_handler
from mks_backend.models.construction_progress import ConstructionProgress
from mks_backend.repositories import DBSession


class ConstructionProgressRepository:

    def get_construction_progress_by_id(self, id: int) -> ConstructionProgress:
        return DBSession.query(ConstructionProgress).get(id)

    @db_error_handler
    def add_construction_progress(self, construction_progress: ConstructionProgress) -> None:
        DBSession.add(construction_progress)
        DBSession.commit()

    def delete_construction_progress(self, construction_progress: ConstructionProgress) -> None:
        DBSession.delete(construction_progress)
        DBSession.commit()

    @db_error_handler
    def update_construction_progress(self, construction_progress: ConstructionProgress) -> None:
        DBSession.query(ConstructionProgress).filter_by(
            construction_progress_id=construction_progress.construction_progress_id).update(
            {
                'construction_objects_id': construction_progress.construction_objects_id,
                'reporting_date': construction_progress.reporting_date,
                'readiness': construction_progress.readiness,
                'people': construction_progress.people,
                'equipment': construction_progress.equipment,
                'progress_statuses_id': construction_progress.progress_statuses_id,
                'update_datetime': construction_progress.update_datetime,
            }
        )
        DBSession.commit()

    def get_all_construction_progresses_by_object(self, object_id: int) -> list:
        return DBSession.query(ConstructionProgress).filter_by(construction_objects_id=object_id). \
            order_by(desc(ConstructionProgress.update_datetime)).all()

    def get_last_construction_progress_by_object(self, object_id: int) -> ConstructionProgress:
        return DBSession.query(ConstructionProgress).filter_by(construction_objects_id=object_id). \
            order_by(desc(ConstructionProgress.update_datetime)).first()
