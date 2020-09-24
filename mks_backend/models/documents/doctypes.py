from sqlalchemy import (
    Column,
    Integer,
    VARCHAR,
    UniqueConstraint,
)

from mks_backend.models import Base


class DocType(Base):

    _tablename_ = 'doctypes'
    doctypes_id = Column(Integer, primary_key=True)
    code = Column(VARCHAR(40), nullable=False)
    fullname = Column(VARCHAR(255), nullable=False)

    __table_args__ = (
        UniqueConstraint(
            'code',
            'fullname',
            name='doctypes_unique'
        ),
    )
