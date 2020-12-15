from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship

from mks_backend.models import Base


class Commission(Base):
    __tablename__ = 'commission'

    commission_id = Column(Integer, primary_key=True)
    code = Column(VARCHAR(20), unique=True, nullable=False)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)

    construction = relationship(
        'Construction',
        back_populates='commission'
    )
