from mks_backend.errors.db_basic_error import db_error_handler

from mks_backend.models.fias import FIAS
from mks_backend.repositories.fias_entity.api import FIASAPIRepository
from mks_backend.repositories.fias_entity.fias import FIASRepository
from mks_backend.services.fias_entity.api import FIASAPIService
from mks_backend.services.fias_entity.utils import get_search_address


class FIASService:

    def __init__(self):
        self.repo = FIASRepository()
        self.service_api = FIASAPIService()
        self.repo_api = FIASAPIRepository()

    def add_address_fias(self, fias):
        search_address = get_search_address(fias)
        if search_address == '':
            return

        aoid = self.get_aoid(search_address)
        if not aoid:
            return None

        fias_db = self.get_fias_by_aoid(aoid)

        if not fias_db:
            fias.aoid = aoid
            self.add_fias(fias)
        else:
            fias = fias_db

        return fias

    def get_fias_by_aoid(self, aoid: str) -> FIAS:
        return self.repo.get_fias_by_aoid(aoid)

    @db_error_handler
    def add_fias(self, fias: FIAS) -> None:
        self.repo.add_fias(fias)

    def get_all_fiases(self) -> list:
        return self.repo.get_all_fiases()

    def get_fias_by_id(self, id: int) -> FIAS:
        return self.repo.get_fias_by_id(id)

    def delete_fias_by_id(self, id: int) -> None:
        self.repo.delete_fias_by_id(id)

    def delete_unnecessary_fias(self, id: int) -> None:
        allowed = self.check_for_links_in_constructions(id)
        if allowed:
            self.repo.delete_fias_by_id(id)

    def check_for_links_in_constructions(self, id: int) -> bool:
        fias = self.get_fias_by_id(id)
        if not fias.constructions:
            return True
        else:
            return False

    def get_aoid(self, search_address: str) -> str:
        return self.service_api.get_aoid(search_address)
