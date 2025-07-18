from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Datos de conexión a la base de datos. Se puede configurar con la variable
# de entorno DATABASE_URL. De forma predeterminada se conecta a SQL Server
# en 127.0.0.1 utilizando las credenciales proporcionadas.
SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mssql+pyodbc://sa:Ladeda78@127.0.0.1/dbCentrex?driver=ODBC+Driver+17+for+SQL+Server",
)

engine_kwargs = {
    "echo": os.getenv("SQLALCHEMY_ECHO", "false").lower() == "true"
}
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
