from mks_backend.repositories.zones_repository import ZoneRepository
from mks_backend.errors.db_basic_error import db_error_handler


class ZoneService:

    def __init__(self):
        self.repo = ZoneRepository()

    def get_all_zones(self):
        return self.repo.get_all_zones()

    def get_zone_by_id(self, id):
        return self.repo.get_zone_by_id(id)

    @db_error_handler
    def add_zone(self, zone):
        self.repo.add_zone(zone)

    def delete_zone_by_id(self, id):
        self.repo.delete_zone_by_id(id)

    @db_error_handler
    def update_zone(self, new_zone):
        self.repo.update_zone(new_zone)