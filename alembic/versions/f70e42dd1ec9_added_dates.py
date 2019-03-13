"""added dates

Revision ID: f70e42dd1ec9
Revises: b6c555e5eaf3
Create Date: 2019-03-13 20:25:00.838762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f70e42dd1ec9'
down_revision = 'b6c555e5eaf3'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('last_active', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('reapplication_date', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('rebutted_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'rebutted_date')
    op.drop_column('users', 'reapplication_date')
    op.drop_column('users', 'last_active')
    # ### end Alembic commands ###
