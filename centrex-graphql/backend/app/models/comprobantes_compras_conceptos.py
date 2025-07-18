from sqlalchemy import Column, Integer, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ComprobanteCompraConcepto(Base):
    __tablename__ = "comprobantes_compras_conceptos"

    id_concepto = Column(Integer, primary_key=True, autoincrement=True)
    id_comprobanteCompra = Column(Integer, ForeignKey("comprobantes_compras.id_comprobanteCompra"), nullable=False)
    id_concepto_compra = Column(Integer, ForeignKey("conceptos_compra.id_concepto_compra"), nullable=False)
    importe = Column(Numeric(18, 3), nullable=False)
