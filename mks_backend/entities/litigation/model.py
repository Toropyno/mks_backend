from sqlalchemy import VARCHAR, Column, Date, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID

from mks_backend.db_schemas import COURTS_SCHEMA, ORGANIZATION_SCHEMA
from mks_backend.session import Base


class Litigation(Base):
    __tablename__ = 'litigation'
    __table_args__ = {'schema': COURTS_SCHEMA}

    litigation_id = Column(Integer, primary_key=True)

    appeal_date = Column(Date(), nullable=False)

    courts_id = Column(
        Integer,
        ForeignKey(
            '{schema}.courts.courts_id'.format(schema=COURTS_SCHEMA), ondelete='CASCADE'
        ),
        nullable=False
    )

    organizations_id = Column(
        UUID,
        ForeignKey('{schema}.organizations.organizations_id'.format(schema=ORGANIZATION_SCHEMA), ondelete='CASCADE'),
        nullable=False
    )

    participant_statuses_id = Column(
        Integer,
        ForeignKey(
            '{schema}.participant_statuses.participant_statuses_id'.format(schema=COURTS_SCHEMA), ondelete='CASCADE'
        ),
        nullable=False
    )

    construction_companies_id = Column(
        Integer,
        ForeignKey('construction_companies.construction_companies_id', ondelete='CASCADE'), nullable=False,)

    participant_other = Column(VARCHAR(1000))

    information = Column(VARCHAR(1000))

    court_decisions_id = Column(
        Integer,
        ForeignKey('{schema}.court_decisions.court_decisions_id'.format(schema=COURTS_SCHEMA), ondelete='CASCADE'),
        nullable=False,
        )

    decision_date = Column(Date(), nullable=False)

    note = Column(VARCHAR(1000))
