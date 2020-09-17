from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship

from mks_backend.models import Base


class ConstructionStage(Base):

    __tablename__ = 'construction_stages'
    construction_stages_id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(VARCHAR(20), unique=True, nullable=False)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)

    construction_object = relationship(
        'ConstructionObject',
        back_populates='construction_stage'
    )
