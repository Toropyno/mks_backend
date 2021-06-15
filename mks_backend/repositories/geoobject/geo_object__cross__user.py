from mks_backend import DBSession
from mks_backend.models.geoobject.geo_object import GeoObject
from mks_backend.models.geoobject.geo_object__cross__user import GeoObjectCrossUser


class GeoObjectCrossUserRepository:

    def __init__(self):
        self._query = DBSession.query(GeoObjectCrossUser)

    def add_geo_object__cross__user(self, geo_object: GeoObjectCrossUser) -> None:
        DBSession.add(geo_object)
        DBSession.commit()

    def get_geo_object_for_user(self, geo_object: GeoObject) -> GeoObjectCrossUser:
        geo_object__cross__users = self._query.filter(GeoObjectCrossUser.origin_id == geo_object.geo_object_id)
        geo_object__cross__users = geo_object__cross__users.filter(GeoObjectCrossUser.user == 1).first()
        return geo_object__cross__users