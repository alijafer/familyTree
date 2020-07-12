"""empty message

Revision ID: 219af26825af
Revises: 452faf7b38da
Create Date: 2020-07-10 01:43:02.947899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '219af26825af'
down_revision = '452faf7b38da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Persons', sa.Column('partenr', sa.Integer(), nullable=True))
    op.add_column('Persons', sa.Column('relation1', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Persons', 'relation1')
    op.drop_column('Persons', 'partenr')
    # ### end Alembic commands ###