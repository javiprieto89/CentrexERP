from sqlalchemy.orm import Session
from app.models.cajas import Caja

def get_caja(db: Session, id_caja: int):
    return db.query(Caja).filter(Caja.id_caja == id_caja).first()

def get_cajas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Caja).offset(skip).limit(limit).all()

def create_caja(db: Session, data):
    caja = Caja(**data)
    db.add(caja)
    db.commit()
    db.refresh(caja)
    return caja

def update_caja(db: Session, id_caja: int, data):
    caja = db.query(Caja).filter(Caja.id_caja == id_caja).first()
    if not caja:
        return None
    for key, value in data.items():
        setattr(caja, key, value)
    db.commit()
    db.refresh(caja)
    return caja

def delete_caja(db: Session, id_caja: int):
    caja = db.query(Caja).filter(Caja.id_caja == id_caja).first()
    if not caja:
        return False
    db.delete(caja)
    db.commit()
    return True
