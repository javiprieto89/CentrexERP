from sqlalchemy.orm import Session
from app.models.paises import Pais

def get_pais(db: Session, id_pais: int):
    return db.query(Pais).filter(Pais.id_pais == id_pais).first()

def get_paises(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Pais).offset(skip).limit(limit).all()

def create_pais(db: Session, data):
    pais = Pais(**data)
    db.add(pais)
    db.commit()
    db.refresh(pais)
    return pais

def update_pais(db: Session, id_pais: int, data):
    pais = db.query(Pais).filter(Pais.id_pais == id_pais).first()
    if not pais:
        return None
    for key, value in data.items():
        setattr(pais, key, value)
    db.commit()
    db.refresh(pais)
    return pais

def delete_pais(db: Session, id_pais: int):
    pais = db.query(Pais).filter(Pais.id_pais == id_pais).first()
    if not pais:
        return False
    db.delete(pais)
    db.commit()
    return True
