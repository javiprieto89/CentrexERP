from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ItemImpuesto(Base):
    __tablename__ = "items_impuestos"

    id_item = Column(Integer, ForeignKey("items.id_item"), primary_key=True)
    id_impuesto = Column(Integer, ForeignKey("impuestos.id_impuesto"), primary_key=True)
