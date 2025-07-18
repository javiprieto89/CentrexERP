from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class SysMoneda(Base):
    __tablename__ = "sysMoneda"

    id_moneda = Column(Integer, primary_key=True, autoincrement=True)
    moneda = Column(String(50), nullable=False)
    activo = Column(Boolean, nullable=False)
