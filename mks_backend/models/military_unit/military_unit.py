from sqlalchemy import (
    Column,
    Integer,
    VARCHAR,
    ForeignKey,
    CHAR,
)
from sqlalchemy.orm import relationship, backref

from mks_backend.session import Base
from mks_backend.db_schemas import MU_SCHEMA


class MilitaryUnit(Base):
    __tablename__ = 'military_unit'
    __table_args__ = {'schema': MU_SCHEMA}

    idMU = Column(Integer, primary_key=True, autoincrement=True)
    vChNumber = Column(VARCHAR(4))
    codeNameMU = Column(VARCHAR(5))

    pidMU = Column(
        Integer,
        ForeignKey(idMU)
    )

    idNameMU = Column(
        Integer,
        ForeignKey('{schema}.namemilitaryunit.idnamemu'.format(schema=MU_SCHEMA)),
        nullable=False
    )

    idPurpose = Column(
        Integer,
        ForeignKey('{schema}.purposemu.idpurpose'.format(schema=MU_SCHEMA), ondelete='CASCADE'),
        nullable=False
    )

    idMilitaryCity = Column(
        Integer,
        ForeignKey('{schema}.militarycity.idmilitarycity'.format(schema=MU_SCHEMA))
    )

    idSortAF = Column(
        VARCHAR(2),
        ForeignKey('{schema}.sortarmedforces.idsortaf'.format(schema=MU_SCHEMA), ondelete='CASCADE'),
        nullable=False
    )

    idCombatArm = Column(
        CHAR(3),
        ForeignKey('{schema}.combatarm.idcombatarm'.format(schema=MU_SCHEMA), ondelete='CASCADE'),
        nullable=False
    )

    # --------- relationships --------- #

    construction = relationship(
        'Construction',
        back_populates='military_unit'
    )

    combat_arm = relationship(
        'Combatarm',
        back_populates='military_unit'
    )

    military_city = relationship(
        'MilitaryCity',
        back_populates='military_unit'
    )

    name_military_unit = relationship(
        'NameMilitaryUnit',
        back_populates='military_unit'
    )

    purpose_m_u = relationship(
        'PurposeMU',
        back_populates='military_unit'
    )

    sort_armed_forces = relationship(
        'SortArmedForces',
        back_populates='military_unit'
    )

    children = relationship(
        'MilitaryUnit',
        cascade='all, delete-orphan',
        backref=backref('parent', remote_side=idMU),
        passive_deletes=True,
    )
