from sqlalchemy import Column, Integer, String, Numeric, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class CcProveedor(Base):
    __tablename__ = "cc_proveedores"

    id_cc = Column(Integer, primary_key=True, autoincrement=True)
    id_proveedor = Column(Integer, ForeignKey("proveedores.id_proveedor"), nullable=False)
    id_moneda = Column(Integer, ForeignKey("sysMoneda.id_moneda"), nullable=False)
    nombre = Column(String(50), nullable=False)
    saldo = Column(Numeric(18, 3), nullable=False)
    activo = Column(Boolean, nullable=False)

    proveedor = relationship("Proveedores", back_populates="cc_proveedores")
    moneda = relationship("SysMoneda")
