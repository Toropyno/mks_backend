from .model import Zone
from mks_backend.session import DBSession

from mks_backend.errors import DBBasicError


class ZoneRepository:

    def __init__(self):
        self._query = DBSession.query(Zone)

    def get_zone_by_id(self, id_: int) -> Zone:
        zone = self._query.get(id_)
        if not zone:
            raise DBBasicError('zone_ad')
        return zone

    def get_all_zones(self) -> list:
        return self._query.order_by(Zone.fullname).all()

    def add_zone(self, zone: Zone) -> None:
        DBSession.add(zone)
        DBSession.commit()

    def delete_zone_by_id(self, id_: int) -> None:
        zone = self.get_zone_by_id(id_)
        DBSession.delete(zone)
        DBSession.commit()

    def update_zone(self, zone: Zone) -> None:
        if DBSession.merge(zone) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('zone_ad')
