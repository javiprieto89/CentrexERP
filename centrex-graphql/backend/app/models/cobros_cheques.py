from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class CobroCheque(Base):
    __tablename__ = "cobros_cheques"

    id_cobro = Column(Integer, ForeignKey("cobros.id_cobro"), primary_key=True)
    id_cheque = Column(Integer, ForeignKey("cheques.id_cheque"), primary_key=True)

    cobro = relationship("Cobros", back_populates="cobros_cheques")
    cheque = relationship("Cheques")
