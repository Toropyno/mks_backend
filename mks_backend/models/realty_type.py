from sqlalchemy import Column, Integer, VARCHAR

from mks_backend.models import Base


class RealtyType(Base):
    __tablename__ = 'realty_types'

    realty_types_id = Column(Integer, primary_key=True)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)
