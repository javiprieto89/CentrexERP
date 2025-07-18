from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class SeparadorDecimal(Base):
    __tablename__ = "separador_decimal"

    id_separador = Column(Integer, primary_key=True, autoincrement=True)
    separador = Column(String(5), nullable=False)
