from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine

from sofistik.database.models import Base
from sofistik.settings import DATABASE_NAME

engine = create_engine(fr'sqlite:///{DATABASE_NAME}')


def create_database() -> None:
    Base.metadata.create_all(engine)

    alembic_cfg = Config(r'.\sofistik\database\alembic\alembic.ini')
    command.stamp(alembic_cfg, "head")
