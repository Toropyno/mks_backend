from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    UniqueConstraint,
)

from mks_backend.models import Base


class ObjectDocument(Base):

    __tablename__ = 'object_documents'
    object_documents_id = Column(Integer, primary_key=True, autoincrement=True)
    construction_objects_id = Column(
        Integer,
        ForeignKey('construction_objects.construction_objects_id', ondelete='CASCADE'),
        nullable=False,
    )
    construction_documents_id = Column(
        Integer,
        ForeignKey('construction_documents.construction_documents_id', ondelete='CASCADE'),
        nullable=False,
    )

    __table_args__ = (
        UniqueConstraint(
            'construction_objects_id',
            'construction_documents_id',
            name='object_documents_unique'
        ),
    )
