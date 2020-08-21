from mks_backend.repositories.zones_repository import ZoneRepository
from mks_backend.errors.db_basic_error import DBBasicError


class ZoneService:

    def __init__(self):
        self.repo = ZoneRepository()

    def get_all_zones(self):
        return self.repo.get_all_zones()

    def get_zone_by_id(self, id):
        return self.repo.get_zone_by_id(id)

    def add_zone(self, zone):
        #raise ValueError('Зона военного городка с таким наименованием уже существует')
        try:
            self.repo.add_zone(zone)
        except DBAPIError as error:
            raise DBBasicError(error)

    def delete_zone_by_id(self, id):
        self.repo.delete_zone_by_id(id)

    def update_zone(self, new_zone):
        #raise ValueError('Зона военного городка с таким наименованием уже существует')
        try:
            self.repo.update_zone(new_zone)
        except DBAPIError as error:
            raise DBBasicError(error)
