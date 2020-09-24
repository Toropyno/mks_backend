from sqlalchemy import (
    Column,
    Integer,
    Float,
    VARCHAR,
)
from sqlalchemy.orm import relationship

from mks_backend.models import Base


class Location(Base):

    __tablename__ = 'location'
    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    zoom = Column(Integer, nullable=False)
    mark = Column(VARCHAR(32), nullable=False, default='00000000000000000000000000000000')

    construction = relationship(
        'Construction',
        back_populates='location'
    )

    construction_object = relationship(
        'ConstructionObject',
        back_populates='location'
    )
