
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:AnaghaOPS2210@db.ncqspuxvxkqvuhbdazba.supabase.co:5432/postgres",
)
DATABASE_SCHEMA = os.getenv("DATABASE_SCHEMA", "ops-schema")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "options": f'-csearch_path="{DATABASE_SCHEMA}",public',
    },
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
