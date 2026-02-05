"""add message content validation

Revision ID: 1c5ff21f2f24
Revises: d39dc5d05d32
Create Date: 2026-02-04 19:32:14.520930

"""
from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '1c5ff21f2f24'
down_revision: Union[str, Sequence[str], None] = 'd39dc5d05d32'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_check_constraint(
        "check_message_text_not_empty",
        "messages",
        "length(trim(text)) > 0",
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("check_message_text_not_empty", "messages", type_="check")
