from sqlalchemy import VARCHAR, Column, Integer

from mks_backend.db_schemas import STATE_CONTRACT_SCHEMA
from mks_backend.session import Base


class ContractStatus(Base):
    __tablename__ = 'contract_statuses'

    __table_args__ = {'schema': STATE_CONTRACT_SCHEMA}

    contract_statuses_id = Column(Integer, primary_key=True)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)
