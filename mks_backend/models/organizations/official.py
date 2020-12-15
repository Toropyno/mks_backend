from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    VARCHAR,
    DATE,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from mks_backend.models import Base, ORGANIZATION_SCHEMA


class Official(Base):
    __tablename__ = 'officials'

    __table_args__ = {'schema': ORGANIZATION_SCHEMA}

    officials_id = Column(Integer, primary_key=True)
    position_name = Column(VARCHAR(255), nullable=False)
    surname = Column(VARCHAR(40), nullable=True)
    firstname = Column(VARCHAR(40), nullable=True)
    middlename = Column(VARCHAR(40))
    begin_date = Column(DATE, nullable=False)
    end_date = Column(DATE)
    phone = Column(VARCHAR(40))
    secure_channel = Column(VARCHAR(40))
    email = Column(VARCHAR(80))
    note = Column(VARCHAR(1000))

    organizations_id = Column(
        UUID,
        ForeignKey('{schema}.organizations.organizations_id'.format(schema=ORGANIZATION_SCHEMA), ondelete='CASCADE'),
        nullable=False
    )

    military_ranks_id = Column(
        Integer,
        ForeignKey('{schema}.military_ranks.military_ranks_id'.format(schema=ORGANIZATION_SCHEMA)),
        nullable=True
    )

    # --------- relationships --------- #

    military_rank = relationship(
        'MilitaryRank',
        back_populates='officials'
    )

    organization = relationship(
        'Organization'
    )
