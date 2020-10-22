from mks_backend.errors.db_basic_error import db_error_handler
from mks_backend.models.fias import FIAS
from mks_backend.repositories.fias_entity.fias import FIASRepository
from mks_backend.services.construction import ConstructionService


class FIASService:

    def __init__(self):
        self.repo = FIASRepository()
        self.service_construction = ConstructionService()

    @db_error_handler
    def add_fias(self, fias: FIAS) -> None:
        self.repo.add_fias(fias)

    def get_all_fiases(self) -> list:
        return self.repo.get_all_fiases()

    def get_fias_by_id(self, id: int) -> FIAS:
        return self.repo.get_fias_by_id(id)

    def get_fias_by_aoid(self, aoid: str) -> FIAS:
        return self.repo.get_fias_by_aoid(aoid)

    def delete_fias_by_id(self, id: int) -> None:
        self.repo.delete_fias_by_id(id)

    def delete_last_fias_by_id_and_construction_id(self, id: int, construction_id: int) -> None:
        allowed = self.check_for_links_in_constructions(id, construction_id)
        if allowed:
            self.repo.delete_fias_by_id(id)

    def check_for_links_in_constructions(self, id: int, construction_id: int) -> bool:
        constructions = self.service_construction.get_constructions_by_id_fias(id)
        if len(constructions) == 1 and (constructions[0].construction_id == construction_id):
            return True
        else:
            return False
