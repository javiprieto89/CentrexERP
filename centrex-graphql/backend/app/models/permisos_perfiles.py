from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class PermisoPerfil(Base):
    __tablename__ = "permisos_perfiles"

    id_permiso = Column(Integer, ForeignKey("permisos.id_permiso"), primary_key=True)
    id_perfil = Column(Integer, ForeignKey("perfiles.id_perfil"), primary_key=True)
