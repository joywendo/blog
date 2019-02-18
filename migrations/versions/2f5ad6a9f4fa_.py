"""empty message

Revision ID: 2f5ad6a9f4fa
Revises: fdb15f6693e2
Create Date: 2019-02-17 21:56:57.579026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f5ad6a9f4fa'
down_revision = 'fdb15f6693e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'profile_pic_path',
               existing_type=sa.VARCHAR(),
               nullable='False')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'profile_pic_path',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###