from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Provincia(Base):
    __tablename__ = "provincias"

    id_provincia = Column(Integer, primary_key=True, autoincrement=True)
    provincia = Column(String(50), nullable=False)
    id_pais = Column(Integer, ForeignKey("paises.id_pais"), nullable=False)
    activo = Column(Boolean, nullable=False)
