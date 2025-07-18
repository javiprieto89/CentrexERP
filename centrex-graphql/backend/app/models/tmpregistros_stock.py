from sqlalchemy import Column, Integer, Date, Numeric, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TmpRegistroStock(Base):
    __tablename__ = "tmpregistros_stock"

    id_tmpRegistroStock = Column(Integer, primary_key=True, autoincrement=True)
    id_item = Column(Integer, ForeignKey("items.id_item"), nullable=False)
    fecha = Column(Date, nullable=False)
    cantidad = Column(Numeric(18, 3), nullable=False)
    operacion = Column(String(50), nullable=False)
    notas = Column(String)
