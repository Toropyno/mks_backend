from .model import MilitaryRank
from .repository import MilitaryRankRepository


class MilitaryRankService:

    def __init__(self):
        self.repo = MilitaryRankRepository()

    def get_all_military_ranks(self) -> list:
        return self.repo.get_all_military_ranks()

    def get_military_rank_by_id(self, id: int) -> MilitaryRank:
        return self.repo.get_military_rank_by_id(id)

    def add_military_rank(self, military_rank: MilitaryRank) -> None:
        self.repo.add_military_rank(military_rank)

    def delete_military_rank_by_id(self, id: int) -> None:
        self.repo.delete_military_rank_by_id(id)

    def update_military_rank(self, new_military_rank: MilitaryRank) -> None:
        self.repo.update_military_rank(new_military_rank)
