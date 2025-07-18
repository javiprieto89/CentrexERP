from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Datos de conexión a SQL Server
SQLALCHEMY_DATABASE_URL = (
    "mssql+pyodbc://sa:Ladeda78@127.0.0.1/dbCentrex?driver=ODBC+Driver+17+for+SQL+Server"
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,
    fast_executemany=True
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