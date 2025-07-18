from sqlalchemy import Column, Integer, String, Numeric, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Impuesto(Base):
    __tablename__ = "impuestos"

    id_impuesto = Column(Integer, primary_key=True, autoincrement=True)
    impuesto = Column(String(50), nullable=False)
    porcentaje = Column(Numeric(5, 2), nullable=False)
    activo = Column(Boolean, nullable=False)
