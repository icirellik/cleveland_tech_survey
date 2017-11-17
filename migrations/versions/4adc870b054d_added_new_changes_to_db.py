"""Added new changes to db

Revision ID: 4adc870b054d
Revises: 198aac62931f
Create Date: 2017-11-14 17:12:53.640618

"""

# revision identifiers, used by Alembic.
revision = '4adc870b054d'
down_revision = '198aac62931f'

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
    op.add_column('users', sa.Column('annual_amount_earned_from_all_tech_activities_combined', sa.VARCHAR(length=32), nullable=True))
    op.drop_column('users', 'total_hours_worked_per_week')
    op.drop_column('users', 'satisfaction_with_compensation')
    op.drop_column('users', 'feedback')
    op.drop_column('users', 'a_customer_calls_late_friday_evening')
    # ### end Alembic commands ###
