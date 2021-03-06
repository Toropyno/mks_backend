from sqlalchemy import VARCHAR, Column, Integer

from mks_backend.session import Base


class Commission(Base):
    __tablename__ = 'commission'

    commission_id = Column(Integer, primary_key=True)
    code = Column(VARCHAR(20), unique=True, nullable=False)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)
    index_number = Column(Integer)
