from enum import Enum as BuiltinEnum

from sqlalchemy import TIMESTAMP, VARCHAR, Column, PrimaryKeyConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.types import Enum

from mks_backend.db_schemas import MIV_SCHEMA
from mks_backend.session import Base


class TypeEnum(BuiltinEnum):
    json = 'json'
    binary = 'binary'


class Storage(Base):
    __tablename__ = 'storage'
    __table_args__ = (
        PrimaryKeyConstraint(
            'uid',
            'type',
            name='storage_pk'
        ),
        {'schema': MIV_SCHEMA}
    )

    uid = Column(UUID, nullable=False)
    type = Column(Enum(TypeEnum))
    sender = Column(VARCHAR(100), nullable=False)
    dt_received = Column(TIMESTAMP, default=func.now(), nullable=False)
