from mks_backend.session import DBSession

from .model import WorkList


class WorkListRepository:

    def __init__(self):
        self._query = DBSession.query(WorkList)

    def get_work_list_for_construction_object(self, construction_object_id: int) -> list:
        return self._query.filter_by(construction_objects_id=construction_object_id).all()

    def add_work_list(self, work_list: WorkList) -> None:
        DBSession.add(work_list)
        DBSession.commit()

    def delete_work_list_by_id(self, id_: int) -> None:
        self._query.filter(WorkList.works_list_id == id_).delete()
        DBSession.commit()

    def update_work_list(self, new_work_list: WorkList) -> None:
        old_work_list = self._query.filter_by(works_list_id=new_work_list.works_list_id)
        old_work_list.update(
            {
                'element_types_id': new_work_list.element_types_id,
                'construction_objects_id': new_work_list.construction_objects_id,
                'weight': new_work_list.weight,
                'element_description': new_work_list.element_description,
                'begin_date': new_work_list.begin_date,
                'end_date': new_work_list.end_date,
                'unit_id': new_work_list.unit_id,
                'plan': new_work_list.plan,
                'fact': new_work_list.fact,
                'work_types_id': new_work_list.work_types_id,
                'work_description': new_work_list.work_description,
                'note': new_work_list.note,
                'relevance_date': new_work_list.relevance_date
            }
        )

        DBSession.commit()

    def get_work_list_by_id(self, id_: int) -> WorkList:
        return self._query.get(id_)
