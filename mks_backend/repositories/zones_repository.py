from mks_backend.models.zones import Zones
from mks_backend.repositories import DBSession


class ZoneRepository:

    @classmethod
    def get_zone_by_id(cls, id):
        return DBSession.query(Zones).get(id)

    def get_all_zones(self):
        return DBSession.query(Zones).all()

    def add_zone(self, zone):
        DBSession.add(zone)
        DBSession.commit()

    def delete_zone_by_id(self, id):
        zone = self.get_zone_by_id(id)
        DBSession.delete(zone)
        DBSession.commit()

    def update_zone(self, zone):
        DBSession.query(Zones).filter_by(zones_id=zone.zones_id).update(
            {'fullname': zone.fullname})
        DBSession.commit()

    def get_zone_by_fullname(self, fullname):
        return DBSession.query(Zones).filter_by(fullname=fullname).first()