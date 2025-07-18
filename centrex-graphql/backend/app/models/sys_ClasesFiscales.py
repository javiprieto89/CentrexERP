from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class SysClaseFiscal(Base):
    __tablename__ = "sys_ClasesFiscales"

    id_claseFiscal = Column(Integer, primary_key=True, autoincrement=True)
    claseFiscal = Column(String(50), nullable=False)
    activo = Column(Boolean, nullable=False)
