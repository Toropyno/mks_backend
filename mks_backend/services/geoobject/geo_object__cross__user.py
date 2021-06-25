from mks_backend.models.geoobject.geo_object import GeoObject
from mks_backend.models.geoobject.geo_object__cross__user import GeoObjectCrossUser
from mks_backend.repositories.geoobject.geo_object__cross__user import GeoObjectCrossUserRepository


class GeoObjectCrossUserService:

    def __init__(self):
        self.repo = GeoObjectCrossUserRepository()

    def add_geo_object(self, geo_object: GeoObjectCrossUser) -> None:
        self.repo.add_geo_object(geo_object)

    def get_geo_object_for_user(self, geo_object: GeoObject) -> GeoObjectCrossUser:
        return self.repo.get_geo_object_for_user(geo_object)
