"""create inital schema

Revision ID: 7171d59da368
Revises: 
Create Date: 2025-01-16 02:34:11.216042

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '7171d59da368'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username", sa.String(20), nullable=False),
        sa.Column("email", sa.String(40), nullable=False),
        sa.Column("password", sa.String(40), nullable=False),
        sa.Column("history", sa.Integer, nullable=True),
        sa.Column("reset_token", sa.String(1000), nullable=True)
    )

def downgrade() -> None:
    op.drop_table("users")
