"""Add ingredients column to restaurant_pizzas

Revision ID: 09b45be0b414
Revises: f47f2c4de64e
Create Date: 2023-09-25 22:28:36.590141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09b45be0b414'
down_revision = 'f47f2c4de64e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ingredients', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.drop_column('ingredients')

    # ### end Alembic commands ###
