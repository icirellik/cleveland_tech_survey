"""Breaking survey answers into a new table

Revision ID: d4e4c95f0d18
Revises: 88893dd5150d
Create Date: 2017-10-15 18:37:03.858319

"""

# revision identifiers, used by Alembic.
revision = 'd4e4c95f0d18'
down_revision = '88893dd5150d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'users', sa.Column('years_of_pro_exp', sa.INTEGER(), nullable=True))
    op.add_column(u'users', sa.Column('jobs', sa.VARCHAR(length=128), nullable=True))
    op.add_column(u'users', sa.Column('tech_role', sa.VARCHAR(length=128), nullable=True))
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column(u'users', 'survey_answers_id')
    op.drop_table('survey_answers')
    # ### end Alembic commands ###