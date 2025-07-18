from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Datos de conexión a la base de datos. Se puede configurar con la variable
# de entorno DATABASE_URL. Por defecto se usa SQLite para facilitar el inicio.
SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./development.db",
)

engine_kwargs = {"echo": True}
if SQLALCHEMY_DATABASE_URL.startswith("mssql+pyodbc"):
    engine_kwargs["fast_executemany"] = True

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    **engine_kwargs,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# ESTA FUNCIÓN DEBE ESTAR PRESENTE
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
