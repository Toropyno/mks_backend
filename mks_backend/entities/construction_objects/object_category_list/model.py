from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship

from mks_backend.session import Base


class ObjectCategoryList(Base):
    __tablename__ = 'object_categories_list'

    __table_args__ = (
        UniqueConstraint(
            'zones_id',
            'object_categories_id',
            name='object_categories_list_unique'
        ),
    )
    object_categories_list_id = Column(Integer, primary_key=True, autoincrement=True)

    zones_id = Column(
        Integer,
        ForeignKey('zones.zones_id', ondelete='CASCADE'),
        nullable=False
    )

    object_categories_id = Column(
        Integer,
        ForeignKey('object_categories.object_categories_id', ondelete='CASCADE'),
        nullable=False
    )

    # --------- relationships --------- #

    object_category = relationship(
        'ObjectCategory'
    )
