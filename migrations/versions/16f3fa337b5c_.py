"""empty message

Revision ID: 16f3fa337b5c
Revises: ce732fb0b1e0
Create Date: 2021-05-17 07:31:42.634613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16f3fa337b5c'
down_revision = 'ce732fb0b1e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###
    op.execute('UPDATE todos SET completed = False where completed IS NULL;')
    op.alter_column('todos', 'completed', nullable=False)
def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###
