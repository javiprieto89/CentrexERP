from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ConsultaPersonalizada(Base):
    __tablename__ = "consultas_personalizadas"

    id_consulta = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    consulta = Column(String, nullable=False)
