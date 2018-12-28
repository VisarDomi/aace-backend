"""messaging system tables

Revision ID: e8637ae073c2
Revises: 281e90ef54a9
Create Date: 2018-12-28 00:36:46.810309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8637ae073c2'
down_revision = '281e90ef54a9'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messagegroups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('sender_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sender_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_messagegroup',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('messagegroup_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['messagegroup_id'], ['messagegroups.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    op.create_table('messagerecipients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_read', sa.Boolean(), nullable=True),
    sa.Column('recipient_id', sa.Integer(), nullable=True),
    sa.Column('recipient_group_id', sa.Integer(), nullable=True),
    sa.Column('message_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['message_id'], ['messages.id'], ),
    sa.ForeignKeyConstraint(['recipient_group_id'], ['messagegroups.id'], ),
    sa.ForeignKeyConstraint(['recipient_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('images', sa.Column('message_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'images', 'messages', ['message_id'], ['id'])
    op.add_column('videos', sa.Column('message_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'videos', 'messages', ['message_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'videos', type_='foreignkey')
    op.drop_column('videos', 'message_id')
    op.drop_constraint(None, 'images', type_='foreignkey')
    op.drop_column('images', 'message_id')
    op.drop_table('messagerecipients')
    op.drop_table('user_messagegroup')
    op.drop_table('messages')
    op.drop_table('messagegroups')
    # ### end Alembic commands ###
