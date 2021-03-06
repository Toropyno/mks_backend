from sqlalchemy import VARCHAR, Column, Float, Integer
from sqlalchemy.orm import relationship

from mks_backend.session import Base


class Coordinate(Base):
    __tablename__ = 'coordinates'

    coordinates_id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    zoom = Column(Integer, nullable=False)
    mark = Column(VARCHAR(40), nullable=False, default='00000000000000000000000000000000')

    construction = relationship(
        'Construction',
        back_populates='coordinate'
    )
