from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


from mks_backend.models import Base


class SubcategoriesList(Base):

    __tablename__ = 'subcategories_list'
    subcategories_list_id = Column(Integer, primary_key=True, autoincrement=True)
    construction_categories_id = Column(
        Integer,
        ForeignKey('construction_categories.construction_categories_id', ondelete='CASCADE'),
        unique=True,
        nullable=False)
    construction_subcategories_id = Column(
        Integer,
        ForeignKey('construction_subcategories.construction_subcategories_id', ondelete='CASCADE'),
        unique=True,
        nullable=False)

    construction_category = relationship(
        'ConstructionCategories',
        back_populates='subcategories_list',
        passive_deletes=True
    )

    construction_subcategory = relationship(
        'ConstructionSubcategories',
        back_populates='subcategories_list',
        passive_deletes=True
    )

    construction = relationship(
        'Construction',
        back_populates='subcategories_list'
    )
