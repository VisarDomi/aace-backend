"""removed a string column from group

Revision ID: 5aeaba63a427
Revises: 41e79aa5358e
Create Date: 2019-03-03 02:32:15.786322

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5aeaba63a427'
down_revision = '41e79aa5358e'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('groups', 'group_picture')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('groups', sa.Column('group_picture', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###