from sqlalchemy import Column, VARCHAR, CHAR
from sqlalchemy.orm import relationship

from mks_backend.session import Base
from mks_backend.db_schemas import MU_SCHEMA


class Combatarm(Base):
    __tablename__ = 'combatarm'
    __table_args__ = {'schema': MU_SCHEMA}

    idcombatarm = Column(CHAR(3), primary_key=True)
    namecombatarm = Column(VARCHAR(255), nullable=False)

    military_unit = relationship(
        'MilitaryUnit',
        back_populates='combat_arm'
    )
