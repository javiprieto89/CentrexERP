from sqlalchemy import Column, Integer, Numeric, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TmpCobroRetencion(Base):
    __tablename__ = "tmpcobros_retenciones"

    id_retencion = Column(Integer, primary_key=True, autoincrement=True)
    id_cobro = Column(Integer, nullable=False)
    id_impuesto = Column(Integer, ForeignKey("impuestos.id_impuesto"), nullable=False)
    total = Column(Numeric(18, 3), nullable=False)
    notas = Column(String)
