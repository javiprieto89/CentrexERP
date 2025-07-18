from sqlalchemy import Column, Integer, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ComprobanteCompraItem(Base):
    __tablename__ = "comprobantes_compras_items"

    id_item = Column(Integer, primary_key=True, autoincrement=True)
    id_comprobanteCompra = Column(Integer, ForeignKey("comprobantes_compras.id_comprobanteCompra"), nullable=False)
    id_item_fk = Column(Integer, ForeignKey("items.id_item"), nullable=False)
    cantidad = Column(Numeric(18, 3), nullable=False)
    precio_unitario = Column(Numeric(18, 3), nullable=False)
    subtotal = Column(Numeric(18, 3), nullable=False)
    total = Column(Numeric(18, 3), nullable=False)
