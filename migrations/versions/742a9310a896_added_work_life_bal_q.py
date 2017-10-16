"""Added work life bal q

Revision ID: 742a9310a896
Revises: 211f35288385
Create Date: 2017-10-16 17:33:34.789633

"""

# revision identifiers, used by Alembic.
revision = '742a9310a896'
down_revision = '211f35288385'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('years_of_pro_exp', sa.INTEGER(), nullable=True))
    op.add_column('users', sa.Column('most_annoying_work_issue', sa.VARCHAR(length=128), nullable=True))
    op.add_column('users', sa.Column('survey_answers_id', sa.INTEGER(), nullable=True))
    op.add_column('users', sa.Column('how_you_found_your_current_job', sa.VARCHAR(length=128), nullable=True))
    op.add_column('users', sa.Column('primary_programming_language_used_at_work', sa.VARCHAR(length=128), nullable=True))
    op.add_column('users', sa.Column('jobs', sa.VARCHAR(length=128), nullable=True))
    op.add_column('users', sa.Column('tech_role', sa.VARCHAR(length=128), nullable=True))
    # ### end Alembic commands ###
