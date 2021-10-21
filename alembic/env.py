"""Pyramid bootstrap environment. """
from alembic import context
from pyramid.paster import setup_logging
from sqlalchemy import engine_from_config

from mks_backend.session import Base
from mks_backend.settings import SETTINGS

from mks_backend.models_meta import *


config = context.config

setup_logging(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    context.configure(url=SETTINGS['sqlalchemy.url'])
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    engine = engine_from_config(SETTINGS, prefix='sqlalchemy.')

    connection = engine.connect()
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        include_schemas=True
    )

    try:
        with context.begin_transaction():
            context.run_migrations()
    finally:
        connection.close()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()