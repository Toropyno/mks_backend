from sqlalchemy import (
    Column,
    Integer,
    VARCHAR
)

from sqlalchemy.orm import relationship

from mks_backend.models import Base


class RemainingAddress(Base):

    __tablename__ = 'remaining_address'

    id = Column(Integer, primary_key=True)
    full_name = Column(VARCHAR(100))

    fias = relationship(
        'FIAS',
        back_populates='remaining_address',
        passive_deletes=True,
    )
