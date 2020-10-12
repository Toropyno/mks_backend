from sqlalchemy import (
    Column,
    Integer,
    VARCHAR
)

from sqlalchemy.orm import relationship

from mks_backend.models import Base


class City(Base):

    __tablename__ = 'city'

    id = Column(Integer, primary_key=True)
    full_name = Column(VARCHAR(100))

    fiases = relationship(
        'FIAS',
        back_populates='city'
    )
