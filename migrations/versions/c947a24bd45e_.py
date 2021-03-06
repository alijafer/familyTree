"""empty message

Revision ID: c947a24bd45e
Revises: 219af26825af
Create Date: 2020-07-11 07:14:47.268445

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c947a24bd45e'
down_revision = '219af26825af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Persons', 'relation1')
    op.drop_column('Persons', 'partenr')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Persons', sa.Column('partenr', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('Persons', sa.Column('relation1', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
