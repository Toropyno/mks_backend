from mks_backend.session import DBSession

from .model import WorkType


class WorkTypeRepository:

    def __init__(self):
        self._query = DBSession.query(WorkType)

    def get_all_work_types(self) -> list:
        return self._query.all()

    def add_work_type(self, work_type: WorkType) -> None:
        DBSession.add(work_type)
        DBSession.commit()

    def delete_work_type_by_id(self, id_: int) -> None:
        self._query.filter(WorkType.work_types_id == id_).delete()
        DBSession.commit()

    def update_work_type(self, new_work_type: WorkType) -> None:
        old_work_type = self._query.filter_by(work_types_id=new_work_type.work_types_id)
        old_work_type.update(
            {
                'fullname': new_work_type.fullname,
                'note': new_work_type.note
            }
        )

        DBSession.commit()

    def get_work_type_by_id(self, id_: int) -> WorkType:
        return self._query.get(id_)
