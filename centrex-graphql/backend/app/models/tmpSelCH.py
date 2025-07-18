from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TmpSelCH(Base):
    __tablename__ = "tmpSelCH"

    id_tmpSelCH = Column(Integer, primary_key=True, autoincrement=True)
    id_cheque = Column(Integer, ForeignKey("cheques.id_cheque"), nullable=False)
