from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Comprobante(Base):
    __tablename__ = "comprobantes"

    id_comprobante = Column(Integer, primary_key=True, autoincrement=True)
    comprobante = Column(String(100), nullable=False)
    id_tipoComprobante = Column(Integer, ForeignKey("tipos_comprobantes.id_tipoComprobante"), nullable=False)
    numeroComprobante = Column(Integer, nullable=False)
    puntoVenta = Column(Integer, nullable=False)
    esFiscal = Column(Boolean)
    esElectronica = Column(Boolean)
    esManual = Column(Boolean)
    esPresupuesto = Column(Boolean)
    activo = Column(Boolean, nullable=False)
    testing = Column(Boolean, nullable=False)
    maxItems = Column(Integer)
    comprobanteRelacionado = Column(Integer)
    esMiPyME = Column(Boolean, nullable=False)
    CBU_emisor = Column(String(22))
    alias_CBU_emisor = Column(String(50))
    anula_MiPyME = Column(String(1))
    contabilizar = Column(Boolean, nullable=False)
    mueveStock = Column(Boolean, nullable=False)
    id_modoMiPyme = Column(Integer, ForeignKey("sys_modoMiPyme.id_modoMiPyme"), nullable=False)
