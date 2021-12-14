from .repository import ClassRankRepository


class ClassRankService:

    def __init__(self, model, repo=ClassRankRepository):
        self.repo = ClassRankRepository()

    def get_all_class_ranks(self) -> list:
        return self.repo.get_all_class_ranks()

    def get_class_rank(self, id_):
        return self.repo.get_class_rank_by_id(id_)

    def add_class_rank(self, instance) -> None:
        self.repo.add_class_rank(instance)

    def delete_class_rank(self, id_) -> None:
        self.repo.delete_class_rank(id_)

    def edit_class_rank(self, instance) -> None:
        self.repo.edit_class_rank(instance)
