from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Caja(Base):
    __tablename__ = "cajas"

    id_caja = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    esCC = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
