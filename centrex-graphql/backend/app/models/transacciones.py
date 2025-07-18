from sqlalchemy import Column, Integer, String, Numeric, Date, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Transaccion(Base):
    __tablename__ = "transacciones"

    id_transaccion = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(Date, nullable=False)
    tipo = Column(String(50), nullable=False)
    id_caja = Column(Integer, ForeignKey("cajas.id_caja"), nullable=False)
    id_cuentaBancaria = Column(Integer, ForeignKey("cuentas_bancarias.id_cuentaBancaria"), nullable=False)
    importe = Column(Numeric(18, 3), nullable=False)
    notas = Column(String)
    activo = Column(Boolean, nullable=False)
