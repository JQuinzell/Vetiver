"""empty message

Revision ID: 4fc37a9c2738
Revises: 398b7648745
Create Date: 2014-11-22 17:05:10.335000

"""

# revision identifiers, used by Alembic.
revision = '4fc37a9c2738'
down_revision = '398b7648745'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('closed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'closed')
    ### end Alembic commands ###