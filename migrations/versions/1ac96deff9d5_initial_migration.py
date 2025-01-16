"""Initial migration

Revision ID: 1ac96deff9d5
Revises: 
Create Date: 2025-01-16 10:28:27.491626

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1ac96deff9d5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('budgets',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('total', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('budgets')
    op.drop_table('users')
    # ### end Alembic commands ###
