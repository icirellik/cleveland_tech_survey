"""Adding to User model

Revision ID: e26e7864df4b
Revises: c5206ec6d840
Create Date: 2017-10-16 08:39:59.356166

"""

# revision identifiers, used by Alembic.
revision = 'e26e7864df4b'
down_revision = 'c5206ec6d840'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('survey_answers_id', sa.INTEGER(), nullable=True))
    op.add_column('users', sa.Column('years_of_pro_exp', sa.INTEGER(), nullable=True))
    op.add_column('users', sa.Column('jobs', sa.VARCHAR(length=128), nullable=True))
    op.add_column('users', sa.Column('tech_role', sa.VARCHAR(length=128), nullable=True))
    op.drop_column('users', 'undergraduate_major')
    # ### end Alembic commands ###