from sqlalchemy import Column, Integer, String, Numeric, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class CuentaBancaria(Base):
    __tablename__ = "cuentas_bancarias"

    id_cuentaBancaria = Column(Integer, primary_key=True, autoincrement=True)
    id_banco = Column(Integer, ForeignKey("bancos.id_banco"), nullable=False)
    nombre = Column(String(50), nullable=False)
    id_moneda = Column(Integer, ForeignKey("sysMoneda.id_moneda"), nullable=False)
    saldo = Column(Numeric(18, 3))
    activo = Column(Boolean, nullable=False)

    banco = relationship("Bancos", back_populates="cuentas_bancarias")
    cheques = relationship("Cheques", back_populates="cuenta_bancaria")
