"""added check_constraints

Revision ID: 0ca3c0b7bbd2
Revises: 2634433bb411
Create Date: 2021-12-07 10:55:13.325616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ca3c0b7bbd2'
down_revision = '2634433bb411'
branch_labels = None
depends_on = None


def upgrade():
    op.create_check_constraint('works_list_weight_check', 'works_list', 'weight > 0 AND weight <= 100')
    op.create_check_constraint('works_list_date_check', 'works_list', 'end_date >= begin_date')
    op.create_check_constraint('works_list_plan_check', 'works_list', 'plan > 0')
    op.create_check_constraint('works_list_fact_check', 'works_list', 'plan >= 0 AND fact < plan')

    op.create_check_constraint('construction_objects_weight_check', 'construction_objects', 'weight > 0 AND weight <= 100')

    op.create_check_constraint('construction_progress_people_plan_check', 'construction_progress', 'people_plan >= 0')
    op.create_check_constraint('construction_progress_equipment_plan_check', 'construction_progress', 'equipment_plan >= 0')
    op.create_check_constraint('construction_progress_readiness_check', 'construction_progress', 'readiness > 0 AND readiness <= 100')
    op.create_check_constraint('construction_progress_people_check', 'construction_progress', 'people >= 0')
    op.create_check_constraint('construction_progress_equipment_check', 'construction_progress', 'equipment >= 0')

    op.create_check_constraint('construction_stages_hierarchy_level_check', 'construction_stages', 'hierarchy_level > 0')

    op.create_check_constraint('construction_hierarchy_level_check', 'construction', 'object_amount > 0')

    op.create_check_constraint('construction_dynamics_people_plan_check', 'construction_dynamics', 'people_plan >= 0')
    op.create_check_constraint('construction_dynamics_people_check', 'construction_dynamics', 'people >= 0')
    op.create_check_constraint('construction_dynamics_equipment_plan_check', 'construction_dynamics', 'equipment_plan >= 0')
    op.create_check_constraint('construction_dynamics_equipment_check', 'construction_dynamics', 'equipment >= 0')

    op.create_check_constraint('organizations_history_date_check', 'organizations_history', 'end_date >= begin_date', schema='organization')


def downgrade():
    op.create_check_constraint('organizations_history_date_check', 'organizations_history', 'end_date >= begin_date', schema='organization')

    op.create_check_constraint('construction_dynamics_equipment_check', 'construction_dynamics', type_='check')
    op.create_check_constraint('construction_dynamics_equipment_plan_check', 'construction_dynamics', type_='check')
    op.create_check_constraint('construction_dynamics_people_check', 'construction_dynamics', type_='check')
    op.create_check_constraint('construction_dynamics_people_plan_check', 'construction_dynamics', type_='check')

    op.create_check_constraint('construction_hierarchy_level_check', 'construction', type_='check')

    op.create_check_constraint('construction_stages_hierarchy_level_check', 'construction_stages', type_='check')

    op.create_check_constraint('construction_progress_equipment_check', 'construction_progress', type_='check')
    op.create_check_constraint('construction_progress_people_check', 'construction_progress', type_='check')
    op.create_check_constraint('construction_progress_readiness_check', 'construction_progress', 'readiness > 0 AND readiness <= 100')
    op.create_check_constraint('construction_progress_equipment_plan_check', 'construction_progress', type_='check')
    op.create_check_constraint('construction_progress_people_plan_check', 'construction_progress', type_='check')

    op.create_check_constraint('construction_objects_weight_check', 'construction_objects', type_='check')

    op.drop_constraint('works_list_fact_check', 'works_list', type_='check')
    op.drop_constraint('works_list_plan_check', 'works_list', type_='check')
    op.drop_constraint('works_list_date_check', 'works_list', type_='check')
    op.drop_constraint('works_list_weight_check', 'works_list', type_='check')
