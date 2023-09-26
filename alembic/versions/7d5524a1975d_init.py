"""init

Revision ID: 7d5524a1975d
Revises: 
Create Date: 2023-09-24 20:14:51.898546

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7d5524a1975d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('autor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=True),
    sa.Column('apellido', sa.String(), nullable=True),
    sa.Column('fecha_nacimiento', sa.Date(), nullable=True),
    sa.Column('pais', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('libro',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titulo', sa.String(), nullable=True),
    sa.Column('autor', sa.Integer(), nullable=True),
    sa.Column('isbn', sa.Integer(), nullable=True),
    sa.Column('genero', sa.String(), nullable=True),
    sa.Column('num_copia', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('isbn')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=True),
    sa.Column('apellido', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('libros_prestados', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuario')
    op.drop_table('libro')
    op.drop_table('autor')
    # ### end Alembic commands ###