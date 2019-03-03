"""third run

Revision ID: b0f7330b28b4
Revises: 5aeaba63a427
Create Date: 2019-03-03 02:56:56.100192

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0f7330b28b4'
down_revision = '5aeaba63a427'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mediaexperiences',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('media_filename', sa.String(), nullable=True),
    sa.Column('media_url', sa.String(), nullable=True),
    sa.Column('experience_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['experience_id'], ['experiences.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mediaskills',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('media_filename', sa.String(), nullable=True),
    sa.Column('media_url', sa.String(), nullable=True),
    sa.Column('skill_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['skill_id'], ['skills.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mediaskills')
    op.drop_table('mediaexperiences')
    # ### end Alembic commands ###