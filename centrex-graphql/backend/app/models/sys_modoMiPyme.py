from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class SysModoMiPyme(Base):
    __tablename__ = "sys_modoMiPyme"

    id_modoMiPyme = Column(Integer, primary_key=True, autoincrement=True)
    modoMiPyme = Column(String(50), nullable=False)
    activo = Column(Boolean, nullable=False)
