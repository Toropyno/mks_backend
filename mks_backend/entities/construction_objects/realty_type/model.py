from sqlalchemy import VARCHAR, Column, Integer

from mks_backend.session import Base


class RealtyType(Base):
    __tablename__ = 'realty_types'

    realty_types_id = Column(Integer, primary_key=True)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)
