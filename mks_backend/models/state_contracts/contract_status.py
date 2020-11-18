from sqlalchemy import (
    Column,
    Integer,
    VARCHAR,
)

from mks_backend.models import Base


class ContractStatus(Base):

    __tablename__ = 'contract_statuses'

    contract_statuses_id = Column(Integer, primary_key=True)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)
