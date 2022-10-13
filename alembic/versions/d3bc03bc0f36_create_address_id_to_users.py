"""create address_id to users

Revision ID: d3bc03bc0f36
Revises: 4073f2d71f0c
Create Date: 2022-10-13 17:58:32.144097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3bc03bc0f36'
down_revision = '4073f2d71f0c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'users',
        sa.Column('address_id', sa.Integer(), nullable=True)
    )
    # create relationship
    op.create_foreign_key('address_users_fk', source_table='users', referent_table='address',
                          local_cols=['address_id'], remote_cols=['id'], ondelete='CASCADE'

                          )


def downgrade() -> None:
    # dropping fk constraint in users table for address_id
    op.drop_constraint(
        'address_users_fk', table_name='users'
    )
    op.drop_column('users', 'address_id')
