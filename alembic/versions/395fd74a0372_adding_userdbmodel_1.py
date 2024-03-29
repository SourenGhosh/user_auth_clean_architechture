"""Adding UserDBModel 1

Revision ID: 395fd74a0372
Revises: 
Create Date: 2024-03-07 20:24:34.602248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '395fd74a0372'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), server_default=sa.text('(false)'), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.String(), server_default='2021-01-01', nullable=True),
    sa.Column('updated_at', sa.String(), server_default='2021-01-01', nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('user_token',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.String(), server_default='2021-01-01', nullable=True),
    sa.Column('updated_at', sa.String(), server_default='2021-01-01', nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_token')
    op.drop_table('users')
    # ### end Alembic commands ###
