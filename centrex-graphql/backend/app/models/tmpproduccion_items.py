from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TmpProduccionItem(Base):
    __tablename__ = "tmpproduccion_items"

    id_tmpProduccion = Column(Integer, primary_key=True)
    id_item = Column(Integer, ForeignKey("items.id_item"), primary_key=True)
    cantidad = Column(Integer, nullable=False)
