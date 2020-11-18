from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    DATE,
    UniqueConstraint,
)

from sqlalchemy.orm import relationship

from mks_backend.models import Base, STATE_CONTRACT_SCHEMA, ORGANIZATION_SCHEMA


class CompletionDate(Base):
    """
    Сроки окончания работ по контракту
    """

    __tablename__ = 'completion_dates'

    __table_args__ = (
        UniqueConstraint(
            'contracts_id',
            'contract_worktypes_id',
            name='completion_dates_unique'
        ),
        {'schema': STATE_CONTRACT_SCHEMA},
    )

    completion_dates_id = Column(Integer, primary_key=True)
    end_date = Column(DATE, nullable=False)

    contracts_id = Column(
        Integer,
        ForeignKey('{schema}.contracts.contracts_id'.format(schema=ORGANIZATION_SCHEMA)),
        nullable=False
    )

    contract_worktypes_id = Column(
        Integer,
        # ForeignKey('{schema}.contract_worktypes.contract_worktypes_id'.format(schema=ORGANIZATION_SCHEMA)),
        nullable=False
    )

    # --------- relationships --------- #

    contract_worktype = relationship(
        'ContractWorkType',
        back_populates='completion_dates'
    )

    # contract = relationship(
    #     'Contract',
    #     back_populates='completion_dates'
    # )
