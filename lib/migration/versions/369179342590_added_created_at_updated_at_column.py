"""added created_at & updated_at column

Revision ID: 369179342590
Revises: 2767c52c266f
Create Date: 2023-09-05 11:23:04.674410

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '369179342590'
down_revision: Union[str, None] = '2767c52c266f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customers', sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
    op.add_column('customers', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('restaurants', sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
    op.add_column('restaurants', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('reviews', sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
    op.add_column('reviews', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reviews', 'updated_at')
    op.drop_column('reviews', 'created_at')
    op.drop_column('restaurants', 'updated_at')
    op.drop_column('restaurants', 'created_at')
    op.drop_column('customers', 'updated_at')
    op.drop_column('customers', 'created_at')
    # ### end Alembic commands ###