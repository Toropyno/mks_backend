from sqlalchemy import DATE, TIMESTAMP, Column, ForeignKey, Integer, UniqueConstraint, func

from mks_backend.session import Base


class ObjectCompletion(Base):
    """
    История изменения сроков
    """

    __tablename__ = 'object_completion'
    __table_args__ = (
        UniqueConstraint(
            'construction_objects_id',
            'planned_date',
            name='object_completion_ak'
        ),
    )

    object_completion_id = Column(Integer, primary_key=True)
    planned_date = Column(DATE, nullable=False)
    update_datetime = Column(TIMESTAMP, default=func.now(), nullable=False)

    construction_objects_id = Column(
        ForeignKey('construction_objects.construction_objects_id', ondelete='CASCADE'), nullable=False
    )
