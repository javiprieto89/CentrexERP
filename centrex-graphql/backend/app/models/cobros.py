from sqlalchemy import Column, Integer, Date, Numeric, Boolean, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Cobro(Base):
    __tablename__ = "cobros"

    id_cobro = Column(Integer, primary_key=True, autoincrement=True)
    id_cobro_oficial = Column(Integer, nullable=False)
    id_cobro_no_oficial = Column(Integer, nullable=False)
    fecha_carga = Column(Date, nullable=False)
    fecha_cobro = Column(Date, nullable=False)
    id_cliente = Column(Integer, ForeignKey("clientes.id_cliente"), nullable=False)
    id_cc = Column(Integer, ForeignKey("cc_clientes.id_cc"), nullable=False)
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
    id_anulaCobro = Column(Integer)
    notas = Column(String)
    firmante = Column(String(50), nullable=False)

    cliente = relationship("Clientes")
    cc_cliente = relationship("CcClientes")
    cobros_cheques = relationship("CobrosCheques", back_populates="cobro")
    cobros_retenciones = relationship("CobrosRetenciones", back_populates="cobro")
