"""initial

Revision ID: 43b74d89606d
Revises: 
Create Date: 2024-01-11 18:04:06.083334

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '43b74d89606d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('login', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('nickname', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('money', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('notes', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_login'), 'users', ['login'], unique=True)
    op.create_table('orders',
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('customer', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('notes', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['customer'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    op.drop_index(op.f('ix_users_login'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###