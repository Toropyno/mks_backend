from sqlalchemy import VARCHAR, Column, Integer
from sqlalchemy.orm import relationship

from mks_backend.session import Base


class ConstructionType(Base):
    __tablename__ = 'construction_types'

    construction_types_id = Column(Integer, primary_key=True)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)

    constructions = relationship(
        'Construction',
        back_populates='construction_type'
    )
