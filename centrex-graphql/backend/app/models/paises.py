from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Pais(Base):
    __tablename__ = "paises"

    id_pais = Column(Integer, primary_key=True, autoincrement=True)
    pais = Column(String(100), nullable=False)
    activo = Column(Boolean, nullable=False)
