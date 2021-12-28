from .model import WorkType
from .repository import WorkTypeRepository


class WorkTypeService:

    def __init__(self):
        self.repo = WorkTypeRepository()

    def get_all_work_types(self) -> list:
        return self.repo.get_all_work_types()

    def get_work_type_by_id(self, id_: int) -> WorkType:
        return self.repo.get_work_type_by_id(id_)

    def add_work_type(self, work_type: WorkType) -> None:
        self.repo.add_work_type(work_type)

    def update_work_type(self, new_work_type: WorkType) -> None:
        self.repo.update_work_type(new_work_type)

    def delete_work_type_by_id(self, id_: int) -> None:
        self.repo.delete_work_type_by_id(id_)
