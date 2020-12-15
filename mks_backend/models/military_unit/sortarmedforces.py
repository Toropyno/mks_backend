from sqlalchemy import (
    Column,
    Integer,
    VARCHAR,
    CHAR,
)
from sqlalchemy.orm import relationship

from mks_backend.models import Base


class SortArmedForces(Base):
    __tablename__ = 'sortarmedforces'

    idsortaf = Column(CHAR(3), primary_key=True)
    namesortaf = Column(VARCHAR(255), nullable=False)
    snamesortaf = Column(VARCHAR(10))

    military_unit = relationship(
        'MilitaryUnit',
        back_populates='sort_armed_forces'
    )
