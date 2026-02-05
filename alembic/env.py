from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import sys

# чтобы работал import app.*
sys.path.append(".")

from app.core.config import settings
from app.core.database import Base
from app.models.chat import Chat
from app.models.message import Message

config = context.config

# логирование
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# metadata для autogenerate
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = settings.database_url
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        {
            "sqlalchemy.url": settings.database_url
        },
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
