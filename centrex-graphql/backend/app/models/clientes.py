from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"

    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    taxNumber = Column(String(50))
    razon_social = Column(String(100), nullable=False)
    nombre_fantasia = Column(String(100))
    contacto = Column(String(100))
    telefono = Column(String(50))
    celular = Column(String(50))
    email = Column(String(100))
    id_provincia_fiscal = Column(Integer, ForeignKey("provincias.id_provincia"))
    direccion_fiscal = Column(String(200))
    localidad_fiscal = Column(String(200))
    cp_fiscal = Column(String(20))
    id_provincia_entrega = Column(Integer, ForeignKey("provincias.id_provincia"))
    direccion_entrega = Column(String(200))
    localidad_entrega = Column(String(200))
    cp_entrega = Column(String(20))
    notas = Column(String)
    esInscripto = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    id_tipoDocumento = Column(Integer, ForeignKey("tipos_documentos.id_tipoDocumento"), nullable=False)
    id_claseFiscal = Column(Integer, ForeignKey("sys_ClasesFiscales.id_claseFiscal"))

    cc_clientes = relationship("CcClientes", back_populates="cliente")
