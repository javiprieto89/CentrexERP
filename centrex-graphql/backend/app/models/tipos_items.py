from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class TipoItem(Base):
    __tablename__ = "tipos_items"

    id_tipo = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String(50), nullable=False)
    activo = Column(Boolean, nullable=False)

    items = relationship("Items", back_populates="tipo")
