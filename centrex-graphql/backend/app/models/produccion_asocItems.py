from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ProduccionAsocItem(Base):
    __tablename__ = "produccion_asocItems"

    id_produccion = Column(Integer, ForeignKey("produccion.id_produccion"), primary_key=True)
    id_item = Column(Integer, ForeignKey("items.id_item"), primary_key=True)
    id_item_asoc = Column(Integer, ForeignKey("items.id_item"), primary_key=True)
    cantidad = Column(Integer, nullable=False)
