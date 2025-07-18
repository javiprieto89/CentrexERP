from sqlalchemy.orm import Session
from app.models.cambios import Cambio

def get_cambio(db: Session, id_cambio: int):
    return db.query(Cambio).filter(Cambio.id_cambio == id_cambio).first()

def get_cambios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Cambio).offset(skip).limit(limit).all()

def create_cambio(db: Session, data):
    cambio = Cambio(**data)
    db.add(cambio)
    db.commit()
    db.refresh(cambio)
    return cambio

def update_cambio(db: Session, id_cambio: int, data):
    cambio = db.query(Cambio).filter(Cambio.id_cambio == id_cambio).first()
    if not cambio:
        return None
    for key, value in data.items():
        setattr(cambio, key, value)
    db.commit()
    db.refresh(cambio)
    return cambio

def delete_cambio(db: Session, id_cambio: int):
    cambio = db.query(Cambio).filter(Cambio.id_cambio == id_cambio).first()
    if not cambio:
        return False
    db.delete(cambio)
    db.commit()
    return True
