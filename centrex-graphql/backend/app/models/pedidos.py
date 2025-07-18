from sqlalchemy import Column, Integer, Date, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Pedido(Base):
    __tablename__ = "pedidos"

    id_pedido = Column(Integer, primary_key=True, autoincrement=True)
    fecha_carga = Column(Date, nullable=False)
    fecha_pedido = Column(Date, nullable=False)
    id_cliente = Column(Integer, ForeignKey("clientes.id_cliente"), nullable=False)
    puntoVenta = Column(String(10))
    numeroPedido = Column(String(50))
    notas = Column(String)
    activo = Column(Boolean, nullable=False)
