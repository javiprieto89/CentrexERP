from sqlalchemy import Column, Integer, Numeric, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class CobroRetencion(Base):
    __tablename__ = "cobros_retenciones"

    id_retencion = Column(Integer, primary_key=True, autoincrement=True)
    id_cobro = Column(Integer, ForeignKey("cobros.id_cobro"), nullable=False)
    id_impuesto = Column(Integer, ForeignKey("impuestos.id_impuesto"), nullable=False)
    total = Column(Numeric(18, 3), nullable=False)
    notas = Column(String)

    cobro = relationship("Cobros", back_populates="cobros_retenciones")
    impuesto = relationship("Impuestos")
