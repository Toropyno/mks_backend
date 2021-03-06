from sqlalchemy import VARCHAR, Column, Integer

from mks_backend.session import Base


class LocationType(Base):
    __tablename__ = 'location_types'

    location_types_id = Column(Integer, primary_key=True)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)
