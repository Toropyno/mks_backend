from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    PrimaryKeyConstraint,
)

from mks_backend.models import Base


class InspectedObject(Base):
    """
    Перечень проверенных объектов
    """
    __tablename__ = 'inspection_objects'

    __table_args__ = (
        PrimaryKeyConstraint(
            'inspections_id',
            'construction_id',
            name='inspection_objects_pk'
        ),
    )

    inspections_id = Column(
        Integer,
        ForeignKey('inspections.inspections_id', ondelete='CASCADE'),
        nullable=False
    )

    construction_id = Column(
        Integer,
        ForeignKey('construction.construction_id', ondelete='CASCADE'),
        nullable=False
    )

    def __str__(self):
        return 'Проверенный объект construction_id={c_id}, проверка inspections_id={insp_id}'.format(
            c_id=self.construction_id,
            insp_id=self.inspections_id
        )
