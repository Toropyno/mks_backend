from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    Column,
    Integer,
    VARCHAR,
    ForeignKey,
    Date,
    DECIMAL,
    CheckConstraint,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

from mks_backend.session import Base


class ConstructionObject(Base):
    __tablename__ = 'construction_objects'

    construction_objects_id = Column(Integer, primary_key=True, autoincrement=True)
    object_code = Column(VARCHAR(40), unique=True, nullable=False)
    object_name = Column(VARCHAR(255), nullable=False)
    generalplan_number = Column(VARCHAR(10))
    building_volume = Column(DECIMAL(17, 3))
    floors_amount = Column(Integer)
    fact_date = Column(Date)

    construction_id = Column(
        Integer,
        ForeignKey('construction.construction_id', ondelete='CASCADE'),
        nullable=False
    )

    weight = Column(
        DECIMAL(5, 2),
        CheckConstraint('weight>0 AND weight<=100'),
        nullable=False
    )

    zones_id = Column(
        Integer,
        ForeignKey('zones.zones_id', ondelete='SET NULL')
    )

    object_categories_list_id = Column(
        Integer,
        ForeignKey('object_categories_list.object_categories_list_id', ondelete='SET NULL')
    )

    construction_stages_id = Column(
        Integer,
        ForeignKey('construction_stages.construction_stages_id', ondelete='SET NULL')
    )

    coordinates_id = Column(
        Integer,
        ForeignKey('coordinates.coordinates_id', ondelete='SET NULL')
    )

    realty_types_id = Column(
        Integer,
        ForeignKey('realty_types.realty_types_id', ondelete='SET NULL'),
        nullable=True
    )

    # --------- relationships --------- #

    construction = relationship(
        'Construction',
        back_populates='construction_objects'
    )

    zone = relationship(
        'Zone',
        back_populates='construction_object'
    )

    object_categories_list = relationship(
        'ObjectCategoryList',
        back_populates='construction_object'
    )

    construction_stage = relationship(
        'ConstructionStage',
        back_populates='construction_object'
    )

    coordinate = relationship(
        'Coordinate',
        back_populates='construction_object'
    )

    construction_progress = relationship(
        'ConstructionProgress',
        back_populates='construction_object',
        cascade='all, delete'
    )

    documents = relationship(
        'ConstructionDocument',
        secondary='object_documents',
        back_populates='parent'
    )

    realty_type = relationship(
        'RealtyType',
    )

    worklist = relationship(
        'WorkList',
        back_populates='construction_object',
        cascade='all, delete'
    )

    object_files = relationship(
        'ObjectFile',
        back_populates='construction_object',
        cascade='all, delete'
    )

    planned_date_query = relationship(
        'ObjectCompletion',
        order_by='desc(ObjectCompletion.planned_date)',
        lazy='dynamic',
        cascade='all, delete'
    )

    # --------- calculated_fields --------- #

    @hybrid_property
    def last_report(self):
        if self.construction_progress:
            return max(self.construction_progress, key=lambda x: x.reporting_date)

    @hybrid_property
    def readiness(self):
        if self.last_report:
            return self.last_report.readiness * Decimal(self.weight) * Decimal(0.01)
        else:
            return 0

    @hybrid_property
    def workers(self):
        if self.last_report:
            return self.last_report.people
        else:
            return 0

    @hybrid_property
    def equipment(self):
        if self.last_report:
            return self.last_report.equipment
        else:
            return 0

    @hybrid_property
    def planned_date(self):
        completion = self.planned_date_query.first()
        return completion.planned_date if completion else None
