from sqlalchemy import (
    Column,
    Integer,
    VARCHAR,
)

from mks_backend.session import Base


class ReasonStopping(Base):
    __tablename__ = 'reason_stopping'

    reasons_stopping_id = Column(Integer, primary_key=True)
    fullname = Column(VARCHAR(255), nullable=False, unique=True, comment='Полное название')
