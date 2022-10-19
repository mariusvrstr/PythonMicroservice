"""added link between user and account entities

Revision ID: 768c1be391cd
Revises: c0e39508b75f
Create Date: 2022-10-18 17:54:54.780033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '768c1be391cd'
down_revision = 'c0e39508b75f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Staff',
    sa.Column('insertDate', sa.DATETIME(), nullable=False),
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False), nullable=False),
    sa.Column('roleLevel', sa.String(length=256), nullable=False),
    sa.Column('staffNumber', sa.String(length=20), nullable=False),
    sa.Column('department', sa.String(), nullable=False),
    sa.Column('jobTitle', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('staffNumber'),
    schema='InoversityLibraryModel'
    )
    op.create_index(op.f('ix_InoversityLibraryModel_Staff_id'), 'Staff', ['id'], unique=False, schema='InoversityLibraryModel')
    op.create_index(op.f('ix_InoversityLibraryModel_Staff_roleLevel'), 'Staff', ['roleLevel'], unique=False, schema='InoversityLibraryModel')
    op.create_table('Student',
    sa.Column('insertDate', sa.DATETIME(), nullable=False),
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False), nullable=False),
    sa.Column('roleLevel', sa.String(length=256), nullable=False),
    sa.Column('studentNumber', sa.String(length=20), nullable=False),
    sa.Column('faculty', sa.String(), nullable=False),
    sa.Column('school', sa.String(), nullable=False),
    sa.Column('programme', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('studentNumber'),
    schema='InoversityLibraryModel'
    )
    op.create_index(op.f('ix_InoversityLibraryModel_Student_id'), 'Student', ['id'], unique=False, schema='InoversityLibraryModel')
    op.create_index(op.f('ix_InoversityLibraryModel_Student_roleLevel'), 'Student', ['roleLevel'], unique=False, schema='InoversityLibraryModel')
    op.add_column('User', sa.Column('accountId', sa.INTEGER(), nullable=True), schema='InoversityLibraryModel')
    op.create_foreign_key(None, 'User', 'Account', ['accountId'], ['id'], source_schema='InoversityLibraryModel', referent_schema='InoversityLibraryModel')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'User', schema='InoversityLibraryModel', type_='foreignkey')
    op.drop_column('User', 'accountId', schema='InoversityLibraryModel')
    op.drop_index(op.f('ix_InoversityLibraryModel_Student_roleLevel'), table_name='Student', schema='InoversityLibraryModel')
    op.drop_index(op.f('ix_InoversityLibraryModel_Student_id'), table_name='Student', schema='InoversityLibraryModel')
    op.drop_table('Student', schema='InoversityLibraryModel')
    op.drop_index(op.f('ix_InoversityLibraryModel_Staff_roleLevel'), table_name='Staff', schema='InoversityLibraryModel')
    op.drop_index(op.f('ix_InoversityLibraryModel_Staff_id'), table_name='Staff', schema='InoversityLibraryModel')
    op.drop_table('Staff', schema='InoversityLibraryModel')
    # ### end Alembic commands ###
