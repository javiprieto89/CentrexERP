from sqlalchemy.orm import Session
from app.models.comprobantes import Comprobante

def get_comprobante(db: Session, id_comprobante: int):
    return db.query(Comprobante).filter(Comprobante.id_comprobante == id_comprobante).first()

def get_comprobantes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Comprobante).offset(skip).limit(limit).all()

def create_comprobante(db: Session, data):
    comprobante = Comprobante(**data)
    db.add(comprobante)
    db.commit()
    db.refresh(comprobante)
    return comprobante

def update_comprobante(db: Session, id_comprobante: int, data):
    comprobante = db.query(Comprobante).filter(Comprobante.id_comprobante == id_comprobante).first()
    if not comprobante:
        return None
    for key, value in data.items():
        setattr(comprobante, key, value)
    db.commit()
    db.refresh(comprobante)
    return comprobante

def delete_comprobante(db: Session, id_comprobante: int):
    comprobante = db.query(Comprobante).filter(Comprobante.id_comprobante == id_comprobante).first()
    if not comprobante:
        return False
    db.delete(comprobante)
    db.commit()
    return True
