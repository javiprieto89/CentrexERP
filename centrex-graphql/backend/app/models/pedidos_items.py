from sqlalchemy import Column, Integer, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class PedidoItem(Base):
    __tablename__ = "pedidos_items"

    id_pedido = Column(Integer, ForeignKey("pedidos.id_pedido"), primary_key=True)
    id_item = Column(Integer, ForeignKey("items.id_item"), primary_key=True)
    cantidad = Column(Numeric(18, 3), nullable=False)
    precio_unitario = Column(Numeric(18, 3), nullable=False)
    subtotal = Column(Numeric(18, 3), nullable=False)
    total = Column(Numeric(18, 3), nullable=False)
