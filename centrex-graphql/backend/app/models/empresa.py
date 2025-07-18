from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Empresa(Base):
    __tablename__ = "empresa"

    id_empresa = Column(Integer, primary_key=True, autoincrement=True)
    razon_social = Column(String(100), nullable=False)
    cuit = Column(String(20), nullable=False)
    domicilio = Column(String(100))
    activo = Column(Boolean, nullable=False)
