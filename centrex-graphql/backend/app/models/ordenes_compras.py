from sqlalchemy import Column, Integer, Date, Numeric, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class OrdenCompra(Base):
    __tablename__ = "ordenes_compras"

    id_ordenCompra = Column(Integer, primary_key=True, autoincrement=True)
    fecha_carga = Column(Date, nullable=False)
    fecha_orden = Column(Date, nullable=False)
    id_proveedor = Column(Integer, ForeignKey("proveedores.id_proveedor"), nullable=False)
    id_moneda = Column(Integer, ForeignKey("sysMoneda.id_moneda"), nullable=False)
    puntoVenta = Column(String(10))
    numeroOrden = Column(String(50))
    subtotal = Column(Numeric(18, 3))
    impuestos = Column(Numeric(18, 3))
    total = Column(Numeric(18, 3))
    tasaCambio = Column(Numeric(18, 3))
    nota = Column(String)
    activo = Column(Boolean, nullable=False)
