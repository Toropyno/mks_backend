from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship

from mks_backend.models import Base


class ObjectCategory(Base):

    __tablename__ = 'object_categories'
    object_categories_id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)
    note = Column(VARCHAR(1000))

    object_categories_list = relationship(
        'ObjectCategoryList',
        back_populates='object_categories_instance',
        passive_deletes=True
    )
