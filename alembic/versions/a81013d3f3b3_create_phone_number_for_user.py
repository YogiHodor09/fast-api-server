"""create phone number for user

Revision ID: a81013d3f3b3
Revises: 
Create Date: 2022-10-13 16:35:51.460634

"""
from tkinter.tix import COLUMN, INTEGER
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a81013d3f3b3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column(
        'phone_number', sa.String(), nullable=True
    ))


def downgrade() -> None:
    op.drop_column(
        'users', 'phone_number'
    )
