"""Bug fixing

Revision ID: 47f47706a830
Revises: 1c98115916d3
Create Date: 2017-11-01 16:39:24.655733

"""

# revision identifiers, used by Alembic.
revision = '47f47706a830'
down_revision = '1c98115916d3'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('jobs', sa.VARCHAR(length=128), nullable=True))
    op.add_column('users', sa.Column('years_of_pro_exp', sa.INTEGER(), nullable=True))
    op.drop_column('users', 'years_of_professional_experience')
    op.drop_column('users', 'work_life_balance')
    op.drop_column('users', 'what_you_value_most_in_compensation')
    op.drop_column('users', 'what_keeps_you_in_cleveland')
    op.drop_column('users', 'undergraduate_major')
    op.drop_column('users', 'tech_roles')
    op.drop_column('users', 'primary_version_control_systems_used_at_work')
    op.drop_column('users', 'primary_programming_languages_used_at_work')
    op.drop_column('users', 'primary_platforms_used_at_work')
    op.drop_column('users', 'primary_development_environments_used_at_work')
    op.drop_column('users', 'primary_database_technologies_used_at_work')
    op.drop_column('users', 'most_annoying_work_issue')
    op.drop_column('users', 'job_satisfaction')
    op.drop_column('users', 'how_you_learned_to_code')
    op.drop_column('users', 'how_you_found_your_current_job')
    op.drop_column('users', 'how_many_days_per_week_you_work_from_home')
    op.drop_column('users', 'highest_educational_attainment')
    op.drop_column('users', 'gender')
    op.drop_column('users', 'favorite_office_perk')
    op.drop_column('users', 'favorite_cleveland_pro_sports_team')
    op.drop_column('users', 'favorite_cleveland_hangout_area')
    op.drop_column('users', 'favorite_cleveland_activity')
    op.drop_column('users', 'ethnicity')
    op.drop_column('users', 'company_size')
    op.drop_column('users', 'annual_amount_earned_from_all_tech_activities_combined')
    # ### end Alembic commands ###