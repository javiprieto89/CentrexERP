from sqlalchemy import Column, Integer, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ComprobanteCompraImpuesto(Base):
    __tablename__ = "comprobantes_compras_impuestos"

    id_impuesto = Column(Integer, primary_key=True, autoincrement=True)
    id_comprobanteCompra = Column(Integer, ForeignKey("comprobantes_compras.id_comprobanteCompra"), nullable=False)
    id_impuesto_fk = Column(Integer, ForeignKey("impuestos.id_impuesto"), nullable=False)
    importe = Column(Numeric(18, 3), nullable=False)
