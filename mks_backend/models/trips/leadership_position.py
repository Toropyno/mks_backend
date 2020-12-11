from sqlalchemy import Column, Integer, VARCHAR

from mks_backend.models import Base


class LeadershipPosition(Base):
    """
    Перечень должностей руководства Министерства обороны РФ
    """
    __tablename__ = 'leadership_positions'

    leadership_positions_id = Column(Integer, primary_key=True)
    code = Column(VARCHAR(40), unique=True, nullable=False)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)
