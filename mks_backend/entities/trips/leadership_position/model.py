from sqlalchemy import VARCHAR, Column, Integer

from mks_backend.session import Base


class LeadershipPosition(Base):
    """
    Перечень должностей руководства Министерства обороны РФ
    """
    __tablename__ = 'leadership_positions'

    leadership_positions_id = Column(Integer, primary_key=True)
    code = Column(VARCHAR(40), unique=True, nullable=False)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)
