"""merging multiple heads

Revision ID: cd801f461cd3
Revises: 3bc72be3c663, c42f6fe33bd9
Create Date: 2018-12-29 16:14:17.963695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd801f461cd3'
down_revision = ('3bc72be3c663', 'c42f6fe33bd9')
branch_labels = None
depends_on = None

def upgrade():
    pass


def downgrade():
    pass
