from sqlalchemy import Column, Integer, VARCHAR

from mks_backend.models import Base


class Commission(Base):

    __tablename__ = 'commission'
    commission_id = Column(Integer, primary_key=True)
    code = Column(VARCHAR(20), nullable=False)
    fullname = Column(VARCHAR(255), nullable=False)
