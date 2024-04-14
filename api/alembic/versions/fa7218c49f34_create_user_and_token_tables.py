"""Create user and token tables

Revision ID: fa7218c49f34
Revises: e5fa7cab21b2
Create Date: 2024-04-13 18:03:07.208993

"""

from typing import Sequence, Union

# revision identifiers, used by Alembic.
revision: str = "fa7218c49f34"
down_revision: Union[str, None] = "e5fa7cab21b2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
