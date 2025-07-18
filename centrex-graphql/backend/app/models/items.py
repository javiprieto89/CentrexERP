from sqlalchemy import Column, Integer, String, Numeric, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Item(Base):
    __tablename__ = "items"

    id_item = Column(Integer, primary_key=True, autoincrement=True)
    item = Column(String(50), nullable=False)
    descript = Column(String(54))
    cantidad = Column(Integer)
    costo = Column(Numeric(18, 6), nullable=False)
    precio_lista = Column(Numeric(18, 6), nullable=False)
    id_tipo = Column(Integer, ForeignKey("tipos_items.id_tipo"), nullable=False)
    id_marca = Column(Integer, ForeignKey("marcas_items.id_marca"), nullable=False)
    id_proveedor = Column(Integer, ForeignKey("proveedores.id_proveedor"), nullable=False)
    factor = Column(Numeric(18, 6))
    esDescuento = Column(Boolean, nullable=False)
    esMarkup = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)

    tipo = relationship("TiposItems", back_populates="items")
    marca = relationship("MarcasItems", back_populates="items")
    proveedor = relationship("Proveedores", back_populates="items")
    ajustes_stock = relationship("AjustesStock", back_populates="item")
    asoc_items = relationship("AsocItems", foreign_keys="[AsocItems.id_item]", back_populates="item")
    asoc_items_asoc = relationship("AsocItems", foreign_keys="[AsocItems.id_item_asoc]", back_populates="item_asoc")
