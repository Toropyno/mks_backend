from uuid import uuid4

from sqlalchemy import BOOLEAN, Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from mks_backend.db_schemas import ORGANIZATION_SCHEMA
from mks_backend.entities.organizations.organization_history import OrganizationHistory
from mks_backend.session import Base


class Organization(Base):
    """
    Организации
    """

    __tablename__ = 'organizations'

    __table_args__ = {'schema': ORGANIZATION_SCHEMA}

    organizations_id = Column(UUID, primary_key=True, default=uuid4)
    par_number = Column(Integer, nullable=True)
    org_sign = Column(BOOLEAN, default=False, nullable=False)

    parent_organizations_id = Column(
        UUID,
        ForeignKey(organizations_id, ondelete='CASCADE'),
        nullable=True
    )

    # --------- relationships --------- #

    history = relationship(
        'OrganizationHistory',
        order_by='desc(OrganizationHistory.begin_date)',
        back_populates='organization',
        passive_deletes=True
    )

    sub_organizations = relationship(
        'Organization',
        passive_deletes=True
    )

    organization_documents = relationship(
        'OrganizationDocument',
        back_populates='organization',
        passive_deletes=True
    )

    officials = relationship(
        'Official',
        back_populates='organization',
        passive_deletes=True
    )

    parent = relationship(
        'Organization',
        remote_side=organizations_id,
        viewonly=True
    )

    # --------- hybrid_properties --------- #

    @hybrid_property
    def children(self) -> list:
        """
        Sorting within the parent is performed by the field "par_number".
        For the same number (or not specified) sorting by the name of a node in the tree.
        """
        return sorted(
            self.sub_organizations,
            key=lambda children: (children.par_number if children.par_number else 0, children.shortname)
        )

    @hybrid_property
    def shortname(self) -> str:
        return self.actual.shortname

    @hybrid_property
    def fullname(self) -> str:
        return self.actual.fullname

    @hybrid_property
    def actual(self) -> OrganizationHistory:
        return max(self.history, key=lambda history_record: history_record.begin_date)

    @hybrid_property
    def is_active(self) -> bool:
        return False if self.actual.end_date else True
