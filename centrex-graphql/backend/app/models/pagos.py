from sqlalchemy import Column, Integer, Date, Numeric, Boolean, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Pago(Base):
    __tablename__ = "pagos"

    id_pago = Column(Integer, primary_key=True, autoincrement=True)
    id_pago_oficial = Column(Integer, nullable=False)
    id_pago_no_oficial = Column(Integer, nullable=False)
    fecha_carga = Column(Date, nullable=False)
    fecha_pago = Column(Date, nullable=False)
    id_proveedor = Column(Integer, ForeignKey("proveedores.id_proveedor"), nullable=False)
    id_cc = Column(Integer, ForeignKey("cc_proveedores.id_cc"), nullable=False)
    dineroEnCc = Column(Numeric(18, 3), nullable=False)
    efectivo = Column(Numeric(18, 3), nullable=False)
    totalTransferencia = Column(Numeric(18, 3), nullable=False)
    totalCh = Column(Numeric(18, 3), nullable=False)
    totalRetencion = Column(Numeric(18, 3), nullable=False)
    total = Column(Numeric(18, 3), nullable=False)
    hayCheque = Column(Boolean, nullable=False)
    hayTransferencia = Column(Boolean, nullable=False)
    hayRetencion = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    id_anulaPago = Column(Integer)
    notas = Column(String)
    firmante = Column(String(50), nullable=False)
