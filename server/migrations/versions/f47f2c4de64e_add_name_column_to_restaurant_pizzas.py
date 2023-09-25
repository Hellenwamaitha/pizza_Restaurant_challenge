"""Add name column to restaurant_pizzas

Revision ID: f47f2c4de64e
Revises: b8ca802a6efc
Create Date: 2023-09-25 22:24:55.207470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f47f2c4de64e'
down_revision = 'b8ca802a6efc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.drop_column('name')

    # ### end Alembic commands ###
