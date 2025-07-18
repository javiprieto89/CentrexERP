from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class MarcaItem(Base):
    __tablename__ = "marcas_items"

    id_marca = Column(Integer, primary_key=True, autoincrement=True)
    marca = Column(String(50), nullable=False)
    activo = Column(Boolean, nullable=False)

    items = relationship("Items", back_populates="marca")
