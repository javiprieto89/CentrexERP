from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class AsocItem(Base):
    __tablename__ = "asocItems"

    id_item = Column(Integer, ForeignKey("items.id_item"), primary_key=True)
    id_item_asoc = Column(Integer, ForeignKey("items.id_item"), primary_key=True)
    cantidad = Column(Integer, nullable=False)

    item = relationship("Items", foreign_keys=[id_item], back_populates="asoc_items")
    item_asoc = relationship("Items", foreign_keys=[id_item_asoc], back_populates="asoc_items_asoc")
