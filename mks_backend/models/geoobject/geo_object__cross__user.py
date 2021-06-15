from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from mks_backend.session import Base


class GeoObjectCrossUser(Base):
    __tablename__ = 'geo_objects__cross__user'

    geo_objects__cross__user_id = Column(Integer, primary_key=True, autoincrement=True)
    origin_id = Column(Integer, ForeignKey('geo_objects.geo_object_id'))
    layer_id = Column(UUID, default=uuid4, nullable=False)
    object_id = Column(UUID, default=uuid4, nullable=False)
    user = Column(Integer, nullable=False, default=1)