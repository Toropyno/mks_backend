from sqlalchemy import CHAR, VARCHAR, Column
from sqlalchemy.orm import relationship

from mks_backend.db_schemas import MU_SCHEMA
from mks_backend.session import Base


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
