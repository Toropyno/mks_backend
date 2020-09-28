from mks_backend.models.work_list import WorkList
from mks_backend.repositories.work_list import WorkListRepository


class WorkListService:

    def __init__(self):
        self.repo = WorkListRepository()

    def get_work_list_for_construction_object(self, construction_object_id: int) -> list:
        return self.repo.get_work_list_for_construction_object(construction_object_id)

    def get_work_list_by_id(self, id: int) -> WorkList:
        return self.repo.get_work_list_by_id(id)

    def add_work_list(self, work_list: WorkList) -> None:
        self.repo.add_work_list(work_list)

    def update_work_list(self, new_work_list: WorkList) -> None:
        self.repo.update_work_list(new_work_list)

    def delete_work_list_by_id(self, id: int) -> None:
        self.repo.delete_work_list_by_id(id)
