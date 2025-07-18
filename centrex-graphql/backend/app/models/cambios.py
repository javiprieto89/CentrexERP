from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Cambio(Base):
    __tablename__ = "cambios"

    id_cambio = Column(Integer, primary_key=True, autoincrement=True)
    cambio = Column(String)
    fecha = Column(Date, nullable=False)
    activo = Column(Boolean, nullable=False)
