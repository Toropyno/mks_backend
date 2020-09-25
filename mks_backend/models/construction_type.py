from sqlalchemy import Column, Integer, VARCHAR

from mks_backend.models import Base


class ConstructionType(Base):

    __tablename__ = 'construction_types'
    construction_types_id = Column(Integer, primary_key=True)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)
