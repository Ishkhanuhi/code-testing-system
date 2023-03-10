"""adding uniqueness to email and username

Revision ID: 7614688d9d9b
Revises: 2b6b89b0eed4
Create Date: 2022-12-17 11:07:19.159204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7614688d9d9b'
down_revision = '2b6b89b0eed4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'users', ['username'])
    op.create_unique_constraint(None, 'users', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_email_key', 'users', type_='unique')
    op.drop_constraint('users_username_key', 'users', type_='unique')
    # ### end Alembic commands ###
