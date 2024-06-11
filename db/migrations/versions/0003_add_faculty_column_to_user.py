"""add faculty column to user

Revision ID: 0003
Revises: 0002
Create Date: 2024-04-12 13:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0003'
down_revision = '0002'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('users', sa.Column('faculty', sa.String(length=255), nullable=True))

def downgrade():
    op.drop_column('users', 'faculty')
