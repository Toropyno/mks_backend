from sqlalchemy import VARCHAR, Column, Integer

from mks_backend.session import Base


class ObjectCategory(Base):
    __tablename__ = 'object_categories'

    object_categories_id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)
    note = Column(VARCHAR(1000))
