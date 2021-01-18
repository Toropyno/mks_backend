from sqlalchemy import (
    Column,
    Integer,
    VARCHAR,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship

from mks_backend.session import Base


class DocType(Base):
    __tablename__ = 'doctypes'

    __table_args__ = (
        UniqueConstraint(
            'code',
            'fullname',
            name='doctypes_unique'
        ),
    )

    doctypes_id = Column(Integer, primary_key=True)
    code = Column(VARCHAR(40), nullable=False)
    fullname = Column(VARCHAR(255), nullable=False)

    # --------- relationships --------- #

    documents = relationship(
        'ConstructionDocument',
        back_populates='doc_type'
    )
