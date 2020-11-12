from mks_backend.models.organizations.official import Official
from mks_backend.repositories.organizations.official import OfficialRepository


class OfficialService:

    def __init__(self):
        self.repo = OfficialRepository()

    def add_official(self, official: Official) -> None:
        self.repo.add_official(official)

    def update_official(self, official: Official) -> None:
        self.repo.update_official(official)

    def delete_official_by_id(self, id: int) -> None:
        self.repo.delete_official(id)
