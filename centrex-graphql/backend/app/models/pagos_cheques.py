from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class PagoCheque(Base):
    __tablename__ = "pagos_cheques"

    id_pago = Column(Integer, ForeignKey("pagos.id_pago"), primary_key=True)
    id_cheque = Column(Integer, ForeignKey("cheques.id_cheque"), primary_key=True)

    pago = relationship("Pagos")
    cheque = relationship("Cheques")
