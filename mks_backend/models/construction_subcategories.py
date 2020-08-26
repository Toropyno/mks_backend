from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship


from mks_backend.models import Base


class ConstructionSubcategories(Base):

    __tablename__ = 'construction_subcategories'
    construction_subcategories_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)

    subcategories_list = relationship(
        'SubcategoriesList',
        back_populates='construction_subcategory',
        passive_deletes=True
    )
