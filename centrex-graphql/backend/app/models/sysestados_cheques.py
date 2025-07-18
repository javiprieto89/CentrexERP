from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class SysEstadoCheque(Base):
    __tablename__ = "sysestados_cheques"

    id_estadoch = Column(Integer, primary_key=True, autoincrement=True)
    estadoch = Column(String(50), nullable=False)
    activo = Column(Boolean, nullable=False)
