from mks_backend.models.zones import Zones
from mks_backend.repositories.zones_repository import ZoneRepository


class ZoneService:

    def __init__(self):
        self.repo = ZoneRepository()

    def get_all_zones(self):
        return self.repo.get_all_zones()

    def get_zone_by_id(self, id):
        return self.repo.get_zone_by_id(id)

    def add_zone(self, zone):
        if self.repo.get_zone_by_fullname(zone.fullname):
            raise ValueError('Зона военного городка с таким наименованием уже существует.')
        self.repo.add_zone(zone)

    def delete_zone_by_id(self, id):
        self.repo.delete_zone_by_id(id)

    def update_zone(self, new_zone):
        self.repo.update_zone(new_zone)

    def get_object(self, json_body):
        zone = Zones()
        if 'id' in json_body:
            zone.zones_id = json_body['id']

        zone.fullname = json_body['fullName']
        return zone
