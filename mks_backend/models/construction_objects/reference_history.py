from sqlalchemy import UniqueConstraint, Column, Integer, ForeignKey, DATE, func
from sqlalchemy.orm import relationship

from mks_backend.session import Base


class ReferenceHistory(Base):
    """
    История принадлежности объекта к ИСП
    """

    __tablename__ = 'references_history'
    __table_args__ = (
        UniqueConstraint(
            'construction_objects_id',
            'construction_id',
            'end_date',
            name='references_history_ak'
        ),
    )

    references_history_id = Column(Integer, primary_key=True)
    end_date = Column(DATE, default=func.now(), nullable=False)

    construction_objects_id = Column(ForeignKey('construction_objects.construction_objects_id', ondelete='CASCADE'), nullable=False)
    construction_id = Column(ForeignKey('construction.construction_id', ondelete='CASCADE'), nullable=False)

    construction = relationship('Construction', lazy='joined', uselist=False)
