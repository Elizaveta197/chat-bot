"""initial migration

Revision ID: 0001
Revises: 
Create Date: 2024-04-12 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Команды для изменения схемы базы данных
    op.create_table('users',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('full_name', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('user_id')
    )

def downgrade():
    # Команды для отката изменений
    op.drop_table('users')
