from sqlalchemy import Column, Integer, Date, Boolean, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Produccion(Base):
    __tablename__ = "produccion"

    id_produccion = Column(Integer, primary_key=True, autoincrement=True)
    fecha_carga = Column(Date, nullable=False)
    fecha = Column(Date, nullable=False)
    notas = Column(String)
    activo = Column(Boolean, nullable=False)
