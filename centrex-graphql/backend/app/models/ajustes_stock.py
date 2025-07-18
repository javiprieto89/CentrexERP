from sqlalchemy import Column, Integer, Date, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class AjusteStock(Base):
    __tablename__ = "ajustes_stock"

    id_ajusteStock = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(Date, nullable=False)
    id_item = Column(Integer, ForeignKey("items.id_item"), nullable=False)
    cantidad = Column(Integer, nullable=False)
    notas = Column(String)

    item = relationship("Items", back_populates="ajustes_stock")
