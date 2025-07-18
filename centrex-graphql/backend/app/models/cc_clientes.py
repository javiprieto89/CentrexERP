from sqlalchemy import Column, Integer, String, Numeric, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class CcCliente(Base):
    __tablename__ = "cc_clientes"

    id_cc = Column(Integer, primary_key=True, autoincrement=True)
    id_cliente = Column(Integer, ForeignKey("clientes.id_cliente"), nullable=False)
    id_moneda = Column(Integer, ForeignKey("sysMoneda.id_moneda"), nullable=False)
    nombre = Column(String(50), nullable=False)
    saldo = Column(Numeric(18, 3), nullable=False)
    activo = Column(Boolean, nullable=False)

    cliente = relationship("Clientes", back_populates="cc_clientes")
    moneda = relationship("SysMoneda")
