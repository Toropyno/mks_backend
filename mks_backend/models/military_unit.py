from sqlalchemy import (
    Column,
    Integer,
    VARCHAR,
    ForeignKey,
    CHAR,
)

from sqlalchemy.orm import relationship, backref

from mks_backend.models import Base


class MilitaryUnit(Base):

    __tablename__ = 'military_unit'
    idMU = Column(Integer, primary_key=True)
    pidMU = Column(Integer, ForeignKey(idMU))
    vChNumber = Column(VARCHAR(4))
    idNameMU = Column(Integer, ForeignKey('name_military_unit.id'), nullable=False)
    idPurpose = Column(Integer, ForeignKey('purpose_m_u.id'), nullable=False)
    idMilitaryCity = Column(Integer, ForeignKey('military_city.id'))
    idSortAF = Column(VARCHAR(2), ForeignKey('sort_armed_forces.id'), nullable=False)
    idCombatArm = Column(CHAR(3), ForeignKey('combat_arm.id'), nullable=False)
    codeNameMU = Column(VARCHAR(5))

    children = relationship(
        "MilitaryUnit",
        cascade="all, delete-orphan",
        backref=backref("parent", remote_side=idMU),
    )

    name_military_unit = relationship(
        "NameMilitaryUnit",
        back_populates='military_unit'
    )

    purpose_m_u = relationship(
        "PurposeMilitaryUnit",
        back_populates='military_unit'
    )

    military_city = relationship(
        "MilitaryCity",
        back_populates='military_unit'
    )

    sort_armed_forces = relationship(
        "SortArmedForces",
        back_populates='military_unit'
    )

    combat_arm = relationship(
        "CombatArm",
        back_populates='military_unit'
    )
