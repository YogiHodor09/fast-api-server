"""create address table

Revision ID: 4073f2d71f0c
Revises: a81013d3f3b3
Create Date: 2022-10-13 17:41:43.169772

"""
from tokenize import String
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4073f2d71f0c'
down_revision = 'a81013d3f3b3'  # previous revision number
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'address',
        sa.Column('id', sa.Integer(),
                  nullable=False, primary_key=True),
        sa.Column('address1', sa.String(),
                  nullable=False),
        sa.Column('address2', sa.String(),
                  nullable=False),
        sa.Column('city', sa.String(),
                  nullable=False),
        sa.Column('state', sa.String(),
                  nullable=False),
        sa.Column('country', sa.String(),
                  nullable=False),
        sa.Column('postal_code', sa.String(),
                  nullable=False)
    )


def downgrade():
    op.drop_table('address')
