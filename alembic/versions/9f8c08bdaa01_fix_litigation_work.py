"""fix_litigation_work

Revision ID: 9f8c08bdaa01
Revises: 4ecbd4700bdb
Create Date: 2022-02-21 11:29:34.206210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f8c08bdaa01'
down_revision = '4ecbd4700bdb'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('litigation', 'construction_companies_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               schema='courts')
    op.alter_column('litigation', 'court_decisions_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               schema='courts')
    op.alter_column('litigation', 'decision_date',
               existing_type=sa.DATE(),
               nullable=True,
               schema='courts')
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('litigation', 'decision_date',
               existing_type=sa.DATE(),
               nullable=False,
               schema='courts')
    op.alter_column('litigation', 'court_decisions_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               schema='courts')
    op.alter_column('litigation', 'construction_companies_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               schema='courts')
    # ### end Alembic commands ###