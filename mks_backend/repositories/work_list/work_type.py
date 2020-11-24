from mks_backend.models.work_list.work_type import WorkType
from mks_backend.models import DBSession

from mks_backend.errors.db_basic_error import db_error_handler


class WorkTypeRepository:

    def __init__(self):
        self._query = DBSession.query(WorkType)

    def get_all_work_types(self) -> list:
        return self._query.all()

    @db_error_handler
    def add_work_type(self, work_type: WorkType) -> None:
        DBSession.add(work_type)
        DBSession.commit()

    def delete_work_type_by_id(self, id: int) -> None:
        self._query.filter(WorkType.work_types_id == id).delete()
        DBSession.commit()

    @db_error_handler
    def update_work_type(self, new_work_type: WorkType) -> None:
        old_work_type = self._query.filter_by(work_types_id=new_work_type.work_types_id)
        old_work_type.update(
            {
                'fullname': new_work_type.fullname,
                'note': new_work_type.note
            }
        )

        DBSession.commit()

    def get_work_type_by_id(self, id: int) -> WorkType:
        return self._query.get(id)
