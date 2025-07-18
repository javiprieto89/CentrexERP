from sqlalchemy import Column, Integer, String, Date, Numeric, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ComprobanteCompra(Base):
    __tablename__ = "comprobantes_compras"

    id_comprobanteCompra = Column(Integer, primary_key=True, autoincrement=True)
    fecha_carga = Column(Date, nullable=False)
    fecha_comprobante = Column(Date, nullable=False)
    id_tipoComprobante = Column(Integer, ForeignKey("tipos_comprobantes.id_tipoComprobante"), nullable=False)
    id_proveedor = Column(Integer, ForeignKey("proveedores.id_proveedor"), nullable=False)
    id_cc = Column(Integer, ForeignKey("cc_proveedores.id_cc"), nullable=False)
    id_moneda = Column(Integer, ForeignKey("sysMoneda.id_moneda"), nullable=False)
    puntoVenta = Column(String(10))
    numeroComprobante = Column(String(50))
    id_condicion_compra = Column(Integer, ForeignKey("condiciones_compra.id_condicion_compra"), nullable=False)
    subtotal = Column(Numeric(18, 3))
    impuestos = Column(Numeric(18, 3))
    conceptos = Column(Numeric(18, 3))
    total = Column(Numeric(18, 3))
    tasaCambio = Column(Numeric(18, 3))
    nota = Column(String)
    cae = Column(String(50))
    activo = Column(Boolean, nullable=False)
