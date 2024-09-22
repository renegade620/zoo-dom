"""remove vet redundnacy

Revision ID: 83f360360c46
Revises: ebd67fbd64d9
Create Date: 2024-09-22 09:55:22.638318

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '83f360360c46'
down_revision: Union[str, None] = 'ebd67fbd64d9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
