from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship, backref

from mks_backend.session import Base


class ConstructionStage(Base):
    __tablename__ = 'construction_stages'

    construction_stages_id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(VARCHAR(20), unique=True, nullable=False)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)
    hierarchy_level = Column(Integer, CheckConstraint('hierarchy_level>0'), nullable=False, default=1)
    ref_construction_stages_id = Column(ForeignKey(construction_stages_id, ondelete='SET NULL'))

    construction_object = relationship(
        'ConstructionObject',
        back_populates='construction_stage'
    )

    children = relationship(
        'ConstructionStage',
        backref=backref('parent', remote_side=construction_stages_id),
        passive_deletes=True,
        uselist=False
    )
