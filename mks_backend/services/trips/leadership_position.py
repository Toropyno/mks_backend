from mks_backend.models.trips.leadership_position import LeadershipPosition
from mks_backend.repositories.trips.leadership_position import LeadershipPositionRepository


class LeadershipPositionService:

    def __init__(self):
        self.repo = LeadershipPositionRepository()

    def get_all_leadership_positions(self) -> list:
        return self.repo.get_all_leadership_positions()

    def get_leadership_position_by_id(self, id: int) -> LeadershipPosition:
        return self.repo.get_leadership_position_by_id(id)

    def add_leadership_position(self, leadership_position: LeadershipPosition) -> None:
        self.repo.add_leadership_position(leadership_position)

    def update_leadership_position(self, new_leadership_position: LeadershipPosition) -> None:
        self.repo.update_leadership_position(new_leadership_position)

    def delete_leadership_position_by_id(self, id: int) -> None:
        self.repo.delete_leadership_position_by_id(id)
