from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class SysClaseComprobante(Base):
    __tablename__ = "sys_claseComprobante"

    id_claseComprobante = Column(Integer, primary_key=True, autoincrement=True)
    claseComprobante = Column(String(50), nullable=False)
    activo = Column(Boolean, nullable=False)
