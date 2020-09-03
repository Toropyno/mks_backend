from sqlalchemy import Column, VARCHAR, CHAR
from sqlalchemy.orm import relationship

from mks_backend.models import Base


class Combatarm(Base):

    __tablename__ = 'combatarm'
    idcombatarm = Column(CHAR(3), primary_key=True)
    namecombatarm = Column(VARCHAR(255), nullable=False)

    military_unit = relationship(
        'MilitaryUnit',
        back_populates='combat_arm'
    )