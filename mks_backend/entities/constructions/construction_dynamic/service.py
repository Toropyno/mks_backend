from typing import List

from .model import ConstructionDynamic
from .repository import ConstructionDynamicRepository


class ConstructionDynamicService:

    def __init__(self):
        self.repo = ConstructionDynamicRepository()

    def get_construction_dynamic_by_id(self, id_: int) -> ConstructionDynamic:
        return self.repo.get_construction_dynamic_by_id(id_)

    def get_construction_dynamics_by_construction_id(self, construction_id: int) -> List[ConstructionDynamic]:
        return self.repo.get_construction_dynamics_by_construction_id(construction_id)

    def add_construction_dynamic(self, construction_dynamic: ConstructionDynamic) -> None:
        self.repo.add_construction_dynamic(construction_dynamic)

    def update_construction_dynamic(self, new_construction_dynamic: ConstructionDynamic) -> None:
        self.repo.update_construction_dynamic(new_construction_dynamic)

    def delete_construction_dynamic_by_id(self, id_: int) -> None:
        self.repo.delete_construction_dynamic(id_)
