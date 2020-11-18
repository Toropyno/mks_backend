from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    UniqueConstraint,
    VARCHAR
)

from mks_backend.models import Base, STATE_CONTRACT_SCHEMA


class ContractWorkType(Base):
    """
    Виды мероприятий по государственным контрактам
    """

    __tablename__ = 'contract_worktypes'

    __table_args__ = (
        {'schema': STATE_CONTRACT_SCHEMA},
    )

    contract_worktypes_id = Column(Integer, primary_key=True)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)
