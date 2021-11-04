"""create quads table

Revision ID: 91fb76bc8019
Revises: 
Create Date: 2021-11-04 01:51:38.324386

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91fb76bc8019'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('quads',
                    sa.Column('id', sa.INTEGER, primary_key=True),
                    sa.Column('quad_number', sa.INTEGER, nullable=False, unique=True),
                    sa.Column('node_0', sa.String, nullable=False),
                    sa.Column('node_1', sa.String, nullable=False),
                    sa.Column('node_2', sa.String, nullable=False),
                    sa.Column('node_3', sa.String, nullable=False),
                    sa.Column('area', sa.INTEGER, nullable=False),
                    sa.Column('plate', sa.INTEGER, nullable=False)
                    )


def downgrade():
    op.drop_table('quads')
