from mks_backend import DBSession
from mks_backend.models.geoobject.geo_object import GeoObject
from mks_backend.models.geoobject.geo_object__cross__user import GeoObjectCrossUser


class GeoObjectRepository:

    def __init__(self):
        self._query = DBSession.query(GeoObject)

    def add_geo_object(self, geo_object: GeoObject) -> None:
        DBSession.add(geo_object)
        DBSession.commit()

    def get_geo_object_for_user(self, geo_object: GeoObject) -> GeoObjectCrossUser:
        geo_object__cross__user_table = self._query.outerjoin(GeoObjectCrossUser)
        geo_object__cross__users = geo_object__cross__user_table.filter(GeoObjectCrossUser.origin_id == geo_object.geo_object_id)
        geo_object__cross__users = geo_object__cross__user_table.filter(GeoObjectCrossUser.user == 1).all()
      #  geo_object__cross__users.all()
#
        return geo_object__cross__users


