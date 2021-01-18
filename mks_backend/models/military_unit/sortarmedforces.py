from sqlalchemy import (
    Column,
    Integer,
    VARCHAR,
    CHAR,
)
from sqlalchemy.orm import relationship

from mks_backend.session import Base
from mks_backend.db_schemas import MU_SCHEMA


class SortArmedForces(Base):
    __tablename__ = 'sortarmedforces'
    __table_args__ = {'schema': MU_SCHEMA}

    idsortaf = Column(CHAR(3), primary_key=True)
    namesortaf = Column(VARCHAR(255), nullable=False)
    snamesortaf = Column(VARCHAR(10))

    military_unit = relationship(
        'MilitaryUnit',
        back_populates='sort_armed_forces'
    )
