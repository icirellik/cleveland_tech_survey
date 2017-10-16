"""Adding co size and job satis qs

Revision ID: 96f7cf9e2d24
Revises: 0e5d053a6897
Create Date: 2017-10-16 15:16:03.348457

"""

# revision identifiers, used by Alembic.
revision = '96f7cf9e2d24'
down_revision = '0e5d053a6897'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('survey_answers_id', sa.INTEGER(), nullable=True))
    op.add_column('users', sa.Column('primary_programming_language_used_at_work', sa.VARCHAR(length=128), nullable=True))
    op.add_column('users', sa.Column('years_of_pro_exp', sa.INTEGER(), nullable=True))
    op.add_column('users', sa.Column('jobs', sa.VARCHAR(length=128), nullable=True))
    op.add_column('users', sa.Column('tech_role', sa.VARCHAR(length=128), nullable=True))
    op.drop_column('users', 'job_satisfaction')
    op.drop_column('users', 'company_size')
    # ### end Alembic commands ###