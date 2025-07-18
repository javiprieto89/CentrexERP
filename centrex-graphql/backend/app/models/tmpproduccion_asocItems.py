from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TmpProduccionAsocItem(Base):
    __tablename__ = "tmpproduccion_asocItems"

    id_tmpProduccion = Column(Integer, primary_key=True)
    id_item = Column(Integer, ForeignKey("items.id_item"), primary_key=True)
    id_item_asoc = Column(Integer, ForeignKey("items.id_item"), primary_key=True)
    cantidad = Column(Integer, nullable=False)
