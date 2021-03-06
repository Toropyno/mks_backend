from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import relationship

from mks_backend.session import Base


class SubcategoryList(Base):
    __tablename__ = 'subcategories_list'

    __table_args__ = (
        UniqueConstraint(
            'construction_categories_id',
            'construction_subcategories_id',
            name='subcategories_list_unique'
        ),
    )

    subcategories_list_id = Column(Integer, primary_key=True, autoincrement=True)

    construction_categories_id = Column(
        Integer,
        ForeignKey('construction_categories.construction_categories_id', ondelete='CASCADE'),
        nullable=False
    )

    construction_subcategories_id = Column(
        Integer,
        ForeignKey('construction_subcategories.construction_subcategories_id', ondelete='CASCADE'),
        nullable=False
    )

    # --------- relationships --------- #

    subcategory = relationship(
        'ConstructionSubcategory'
    )
