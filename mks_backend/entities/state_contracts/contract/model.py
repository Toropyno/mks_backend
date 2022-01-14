from sqlalchemy import DATE, DECIMAL, VARCHAR, Column, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import relationship

from mks_backend.db_schemas import STATE_CONTRACT_SCHEMA
from mks_backend.session import Base


class Contract(Base):
    """
    Сведения о государственных контрактах
    """

    __tablename__ = 'contracts'

    __table_args__ = (
        UniqueConstraint(
            'contract_num',
            'identifier',
            name='contracts_ak'
        ),
        {'schema': STATE_CONTRACT_SCHEMA}
    )

    contracts_id = Column(Integer, primary_key=True)
    contract_num = Column(VARCHAR(50))
    contract_date = Column(DATE, nullable=False)
    identifier = Column(VARCHAR(25))
    subject = Column(VARCHAR(1000))

    contract_sum = Column(DECIMAL(20, 2), default=0, nullable=False)
    paid_sum = Column(DECIMAL(20, 2), default=0, nullable=False)
    accepted_sum = Column(DECIMAL(20, 2), default=0, nullable=False)
    receivables = Column(DECIMAL(20, 2), default=0, nullable=False)
    plan_sum = Column(DECIMAL(20, 2), default=0, nullable=False)

    construction_id = Column(
        Integer,
        ForeignKey('construction.construction_id', ondelete='CASCADE'),
        nullable=False
    )

    contractor_id = Column(
        Integer,
        ForeignKey('construction_companies.construction_companies_id'),
        nullable=False
    )

    subcontractor_id = Column(
        Integer,
        ForeignKey('construction_companies.construction_companies_id'),
    )

    contract_statuses_id = Column(
        Integer,
        ForeignKey('{schema}.contract_statuses.contract_statuses_id'.format(schema=STATE_CONTRACT_SCHEMA)),
        nullable=False
    )

    # --------- relationships --------- #

    construction = relationship(
        'Construction',
        back_populates='contracts'
    )

    contractor = relationship(
        'ConstructionCompany',
        foreign_keys=[contractor_id]
    )

    subcontractor = relationship(
        'ConstructionCompany',
        foreign_keys=[subcontractor_id]
    )

    status = relationship(
        'ContractStatus'
    )

    completion_dates = relationship(
        'CompletionDate'
    )
