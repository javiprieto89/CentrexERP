from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TipoDocumento(Base):
    __tablename__ = "tipos_documentos"

    id_tipoDocumento = Column(Integer, primary_key=True, autoincrement=True)
    tipoDocumento = Column(String(50), nullable=False)
    activo = Column(Boolean, nullable=False)
