from sqlalchemy import Column, Integer, String, Boolean
from app.db import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    usuario = Column(String(20), nullable=False)      # nvarchar(20)
    password = Column(String(50), nullable=False)     # nvarchar(50)
    nombre = Column(String(50), nullable=False)       # nvarchar(50)
    activo = Column(Boolean, nullable=False)
    logueado = Column(Boolean, nullable=False)
