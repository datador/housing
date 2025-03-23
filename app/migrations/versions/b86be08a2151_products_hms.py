"""products, hms

Revision ID: b86be08a2151
Revises:
Create Date: 2025-03-23 16:55:37.217513

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'b86be08a2151'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_hms_faerslunumer', table_name='hms')
    op.drop_index('ix_hms_skjalanumer', table_name='hms')
    op.drop_table('hms')
    op.drop_index('ix_products_manufacturer', table_name='products')
    op.drop_index('ix_products_name', table_name='products')
    op.drop_index('ix_products_year', table_name='products')
    op.drop_table('products')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), autoincrement=False, nullable=False),
    sa.Column('manufacturer', sa.VARCHAR(length=64), autoincrement=False, nullable=False),
    sa.Column('year', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('country', sa.VARCHAR(length=32), autoincrement=False, nullable=True),
    sa.Column('cpu', sa.VARCHAR(length=32), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_products')
    )
    op.create_index('ix_products_year', 'products', ['year'], unique=False)
    op.create_index('ix_products_name', 'products', ['name'], unique=True)
    op.create_index('ix_products_manufacturer', 'products', ['manufacturer'], unique=False)
    op.create_table('hms',
    sa.Column('faerslunumer', sa.VARCHAR(length=6), autoincrement=False, nullable=False),
    sa.Column('emnr', sa.VARCHAR(length=3), autoincrement=False, nullable=False),
    sa.Column('skjalanumer', sa.VARCHAR(length=13), autoincrement=False, nullable=False),
    sa.Column('fastnum', sa.VARCHAR(length=7), autoincrement=False, nullable=False),
    sa.Column('heimilisfang', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('postnr', sa.VARCHAR(length=3), autoincrement=False, nullable=True),
    sa.Column('heinum', sa.VARCHAR(length=7), autoincrement=False, nullable=True),
    sa.Column('svfn', sa.VARCHAR(length=4), autoincrement=False, nullable=False),
    sa.Column('sveitarfelag', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('utgdag', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('thinglystdags', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('kaupverd', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('fasteignamat', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('fasteignamat_gildandi', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('fyrirhugad_fasteignamat', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('brunabotamat_gildandi', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('byggar', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('fepilog', sa.VARCHAR(length=6), autoincrement=False, nullable=False),
    sa.Column('einflm', sa.NUMERIC(), autoincrement=False, nullable=False),
    sa.Column('lod_flm', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('lod_flmein', sa.VARCHAR(length=2), autoincrement=False, nullable=True),
    sa.Column('fjherb', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('tegund', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('fullbuid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('onothaefur_samningur', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('faerslunumer', 'fastnum', name='pk_hms')
    )
    op.create_index('ix_hms_skjalanumer', 'hms', ['skjalanumer'], unique=False)
    op.create_index('ix_hms_faerslunumer', 'hms', ['faerslunumer'], unique=False)
    # ### end Alembic commands ###
