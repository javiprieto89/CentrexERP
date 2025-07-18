from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UsuarioPerfil(Base):
    __tablename__ = "usuarios_perfiles"

    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), primary_key=True)
    id_perfil = Column(Integer, ForeignKey("perfiles.id_perfil"), primary_key=True)
