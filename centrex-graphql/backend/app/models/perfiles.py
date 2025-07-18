from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Perfil(Base):
    __tablename__ = "perfiles"

    id_perfil = Column(Integer, primary_key=True, autoincrement=True)
    perfil = Column(String(50), nullable=False)
    activo = Column(Boolean, nullable=False)
