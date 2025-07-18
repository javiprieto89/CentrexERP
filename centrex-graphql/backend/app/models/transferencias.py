from sqlalchemy import Column, Integer, Numeric, Date, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Transferencia(Base):
    __tablename__ = "transferencias"

    id_transferencia = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(Date, nullable=False)
    id_cuentaBancaria_origen = Column(Integer, ForeignKey("cuentas_bancarias.id_cuentaBancaria"), nullable=False)
    id_cuentaBancaria_destino = Column(Integer, ForeignKey("cuentas_bancarias.id_cuentaBancaria"), nullable=False)
    importe = Column(Numeric(18, 3), nullable=False)
