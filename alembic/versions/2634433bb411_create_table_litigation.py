"""Create Table litigation

Revision ID: 2634433bb411
Revises: d53cbeae0702
Create Date: 2021-10-29 17:58:46.677379

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2634433bb411'
down_revision = 'd53cbeae0702'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('litigation',
    sa.Column('litigation_id', sa.Integer(), nullable=False),
    sa.Column('appeal_date', sa.Date(), nullable=False),
    sa.Column('courts_id', sa.Integer(), nullable=False),
    sa.Column('organizations_id', postgresql.UUID(), nullable=False),
    sa.Column('participant_statuses_id', sa.Integer(), nullable=False),
    sa.Column('construction_companies_id', sa.Integer(), nullable=False),
    sa.Column('participant_other', sa.VARCHAR(length=1000), nullable=True),
    sa.Column('information', sa.VARCHAR(length=1000), nullable=True),
    sa.Column('court_decisions_id', sa.Integer(), nullable=False),
    sa.Column('decision_date', sa.Date(), nullable=False),
    sa.Column('note', sa.VARCHAR(length=1000), nullable=True),
    sa.ForeignKeyConstraint(['construction_companies_id'], ['construction_companies.construction_companies_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['court_decisions_id'], ['courts.court_decisions.court_decisions_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['courts_id'], ['courts.courts.courts_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['organizations_id'], ['organization.organizations.organizations_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['participant_statuses_id'], ['courts.participant_statuses.participant_statuses_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('litigation_id'),
    schema='courts'
    )
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('litigation', schema='courts')
    # ### end Alembic commands ###
