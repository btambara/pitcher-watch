"""add table for player pitches

Revision ID: 84d8b9bda6ab
Revises: d6b02888e79c
Create Date: 2024-02-25 15:43:16.801837

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84d8b9bda6ab'
down_revision: Union[str, None] = 'd6b02888e79c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
