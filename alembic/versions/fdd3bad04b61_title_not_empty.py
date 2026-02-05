"""title not empty

Revision ID: fdd3bad04b61
Revises: 955d2b28d953
Create Date: 2026-02-04 19:21:09.707529

"""
from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'fdd3bad04b61'
down_revision: Union[str, Sequence[str], None] = '955d2b28d953'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_check_constraint(
        "check_chat_title_not_empty",
        "chats",
        "length(trim(title)) > 0",
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("check_chat_title_not_empty", "chats", type_="check")
