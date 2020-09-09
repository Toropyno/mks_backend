from sqlalchemy import (
    Column,
    Integer,
    Float,
    VARCHAR,
    ForeignKey,
    CHAR,
)

from sqlalchemy.orm import relationship

from mks_backend.models import Base


class Location(Base):

    __tablename__ = 'location'
    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float)
    longitude = Column(Float)
    zoom = Column(Integer)
    mark = Column(VARCHAR(32))


    construction = relationship(
        'Construction',
        back_populates='location'
    )

    construction_object = relationship(
        'ConstructionObject',
        back_populates='location'
    )
