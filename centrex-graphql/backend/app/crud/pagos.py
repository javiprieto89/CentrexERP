from sqlalchemy.orm import Session
from app.models.pagos import Pago

def get_pago(db: Session, id_pago: int):
    return db.query(Pago).filter(Pago.id_pago == id_pago).first()

def get_pagos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Pago).offset(skip).limit(limit).all()

def create_pago(db: Session, data):
    pago = Pago(**data)
    db.add(pago)
    db.commit()
    db.refresh(pago)
    return pago

def update_pago(db: Session, id_pago: int, data):
    pago = db.query(Pago).filter(Pago.id_pago == id_pago).first()
    if not pago:
        return None
    for key, value in data.items():
        setattr(pago, key, value)
    db.commit()
    db.refresh(pago)
    return pago

def delete_pago(db: Session, id_pago: int):
    pago = db.query(Pago).filter(Pago.id_pago == id_pago).first()
    if not pago:
        return False
    db.delete(pago)
    db.commit()
    return True
