"""empty message

Revision ID: 452faf7b38da
Revises: 
Create Date: 2020-07-04 00:50:28.003698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '452faf7b38da'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Relations', sa.Column('person', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Relations', 'Persons', ['person'], ['person_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Relations', type_='foreignkey')
    op.drop_column('Relations', 'person')
    # ### end Alembic commands ###
