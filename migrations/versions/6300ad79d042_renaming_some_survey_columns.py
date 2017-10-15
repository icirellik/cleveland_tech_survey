"""renaming some survey columns

Revision ID: 6300ad79d042
Revises: 5ae9c75d0cc6
Create Date: 2017-10-15 14:53:25.132522

"""

# revision identifiers, used by Alembic.
revision = '6300ad79d042'
down_revision = '5ae9c75d0cc6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('tech_role', sa.String(length=128), nullable=True))
    op.add_column('users', sa.Column('years_of_professional_experience', sa.Integer(), nullable=True))
    op.drop_column('users', 'years_of_pro_exp')
    op.drop_column('users', 'jobs')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('jobs', sa.VARCHAR(length=128), nullable=True))
    op.add_column('users', sa.Column('years_of_pro_exp', sa.INTEGER(), nullable=True))
    op.drop_column('users', 'years_of_professional_experience')
    op.drop_column('users', 'tech_role')
    # ### end Alembic commands ###
