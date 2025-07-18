from sqlalchemy.orm import Session
from app.models.pagos_cheques import PagoCheque

def get_pago_cheque(db: Session, id_pago_cheque: int):
    return db.query(PagoCheque).filter(PagoCheque.id_pago_cheque == id_pago_cheque).first()

def get_pagos_cheques(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PagoCheque).offset(skip).limit(limit).all()

def create_pago_cheque(db: Session, data):
    pago = PagoCheque(**data)
    db.add(pago)
    db.commit()
    db.refresh(pago)
    return pago

def update_pago_cheque(db: Session, id_pago_cheque: int, data):
    pago = db.query(PagoCheque).filter(PagoCheque.id_pago_cheque == id_pago_cheque).first()
    if not pago:
        return None
    for key, value in data.items():
        setattr(pago, key, value)
    db.commit()
    db.refresh(pago)
    return pago

def delete_pago_cheque(db: Session, id_pago_cheque: int):
    pago = db.query(PagoCheque).filter(PagoCheque.id_pago_cheque == id_pago_cheque).first()
    if not pago:
        return False
    db.delete(pago)
    db.commit()
    return True
