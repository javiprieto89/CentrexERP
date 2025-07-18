from sqlalchemy import Column, Integer, Date, Numeric, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Cheque(Base):
    __tablename__ = "cheques"

    id_cheque = Column(Integer, primary_key=True, autoincrement=True)
    fecha_ingreso = Column(Date, nullable=False)
    fecha_emision = Column(Date, nullable=False)
    id_cliente = Column(Integer, ForeignKey("clientes.id_cliente"))
    id_proveedor = Column(Integer, ForeignKey("proveedores.id_proveedor"))
    id_banco = Column(Integer, ForeignKey("bancos.id_banco"), nullable=False)
    nCheque = Column(Integer, nullable=False)
    nCheque2 = Column(Integer, nullable=False)
    importe = Column(Numeric(18, 3), nullable=False)
    id_estadoch = Column(Integer, ForeignKey("sysestados_cheques.id_estadoch"), nullable=False)
    fecha_cobro = Column(Date)
    fecha_salida = Column(Date)
    fecha_deposito = Column(Date)
    recibido = Column(Boolean)
    emitido = Column(Boolean)
    id_cuentaBancaria = Column(Integer, ForeignKey("cuentas_bancarias.id_cuentaBancaria"))
    eCheck = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)

    banco = relationship("Bancos", back_populates="cheques")
    cuenta_bancaria = relationship("CuentasBancarias", back_populates="cheques")
    cliente = relationship("Clientes")
    proveedor = relationship("Proveedores")
    estado_cheque = relationship("SysEstadosCheques")
