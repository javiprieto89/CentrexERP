from sqlalchemy import Column, Integer, Numeric
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TmpTransferencia(Base):
    __tablename__ = "tmptransferencias"

    id_tmpTransferencia = Column(Integer, primary_key=True, autoincrement=True)
    importe = Column(Numeric(18, 3), nullable=False)
