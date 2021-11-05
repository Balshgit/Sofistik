from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine

from sofistik.database.models import Base
from sofistik.settings import DATABASE_NAME
from sofistik.utils import logger

engine = create_engine(fr'sqlite:///{DATABASE_NAME}')


def run_migrations() -> None:
    """
    Run alembic migrations

    :return: Update database to last migration
    """
    try:
        alembic_cfg = Config(r'.\sofistik\database\alembic\alembic.ini')
        command.stamp(alembic_cfg, "head")
    except Exception as e:
        logger.error(f'Cant run migrations: {e}')


def create_database() -> None:
    """
    Create database with tables from models

    :return: Insert tables in database
    """
    Base.metadata.create_all(engine)
