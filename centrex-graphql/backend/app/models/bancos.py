from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Banco(Base):
    __tablename__ = "bancos"

    id_banco = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    id_pais = Column(Integer, ForeignKey("paises.id_pais"), nullable=False)
    n_banco = Column(Integer)
    activo = Column(Boolean, nullable=False)

    cuentas_bancarias = relationship("CuentasBancarias", back_populates="banco")
    cheques = relationship("Cheques", back_populates="banco")
