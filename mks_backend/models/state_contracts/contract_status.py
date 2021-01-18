from sqlalchemy import (
    Column,
    Integer,
    VARCHAR,
)

from mks_backend.session import Base
from mks_backend.db_schemas import STATE_CONTRACT_SCHEMA


class ContractStatus(Base):
    __tablename__ = 'contract_statuses'

    __table_args__ = {'schema': STATE_CONTRACT_SCHEMA}

    contract_statuses_id = Column(Integer, primary_key=True)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)
