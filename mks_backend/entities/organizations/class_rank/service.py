from typing import List

from .repository import ClassRankRepository
from .model import ClassRank


class ClassRankService:

    def __init__(self, model, repo=ClassRankRepository):
        self.repo = ClassRankRepository()

    def get_all_class_ranks(self) -> List[ClassRank]:
        return self.repo.get_all_class_ranks()

    def get_class_rank(self, id_) -> ClassRank:
        return self.repo.get_class_rank_by_id(id_)

    def add_class_rank(self, instance) -> None:
        self.repo.add_class_rank(instance)

    def delete_class_rank(self, id_) -> None:
        self.repo.delete_class_rank(id_)

    def update_class_rank(self, instance) -> None:
        self.repo.update_class_rank(instance)
