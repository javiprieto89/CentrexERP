from sqlalchemy import Column, Integer, Date, Numeric, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class CobroNFacturaImporte(Base):
    __tablename__ = "cobros_Nfacturas_importes"

    id_cobro = Column(Integer, ForeignKey("cobros.id_cobro"), primary_key=True)
    fecha = Column(Date, primary_key=True)
    nfactura = Column(String(50), primary_key=True)
    importe = Column(Numeric(18, 6), nullable=False)
