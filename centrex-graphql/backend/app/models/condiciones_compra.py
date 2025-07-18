from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class CondicionCompra(Base):
    __tablename__ = "condiciones_compra"

    id_condicion_compra = Column(Integer, primary_key=True, autoincrement=True)
    condicion = Column(String(50), nullable=False)
    activo = Column(Boolean, nullable=False)
