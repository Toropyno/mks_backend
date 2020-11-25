from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    UniqueConstraint,
    VARCHAR,
    DATE,
    CheckConstraint
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from mks_backend.models import Base, ORGANIZATION_SCHEMA


class OrganizationHistory(Base):
    """
    Организации (история изменений)
    """

    __tablename__ = 'organizations_history'

    __table_args__ = (
        UniqueConstraint(
            'organizations_id',
            'begin_date',
            name='organizations_history_ak'
        ),
        {'schema': ORGANIZATION_SCHEMA},
    )

    organizations_history_id = Column(Integer, primary_key=True)
    shortname = Column(VARCHAR(255), nullable=False)
    fullname = Column(VARCHAR(1000), nullable=False)
    address_legal = Column(VARCHAR(1000), nullable=True)
    address_actual = Column(VARCHAR(1000), nullable=True)
    functions = Column(VARCHAR(2000), nullable=True)

    inn = Column(VARCHAR(20), nullable=True)
    kpp = Column(VARCHAR(20), nullable=True)
    ogrn = Column(VARCHAR(20), nullable=True)

    begin_date = Column(DATE, nullable=False)
    end_date = Column(DATE, CheckConstraint('end_date >= begin_date'), nullable=True)

    organizations_id = Column(
        UUID,
        ForeignKey('{schema}.organizations.organizations_id'.format(schema=ORGANIZATION_SCHEMA), ondelete='CASCADE'),
        nullable=False
    )

    organization = relationship(
        'Organization',
        back_populates='history'
    )
