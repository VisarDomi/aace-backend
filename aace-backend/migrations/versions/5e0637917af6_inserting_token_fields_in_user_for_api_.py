"""inserting token fields in User for api auth

Revision ID: 5e0637917af6
Revises: cd801f461cd3
Create Date: 2018-12-29 16:15:25.722604

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e0637917af6'
down_revision = 'cd801f461cd3'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('token', sa.String(), nullable=True))
    op.add_column('users', sa.Column('token_expiration', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_users_token'), 'users', ['token'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_token'), table_name='users')
    op.drop_column('users', 'token_expiration')
    op.drop_column('users', 'token')
    # ### end Alembic commands ###
