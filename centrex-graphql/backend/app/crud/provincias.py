from sqlalchemy.orm import Session
from app.models.provincias import Provincia

def get_provincia(db: Session, id_provincia: int):
    return db.query(Provincia).filter(Provincia.id_provincia == id_provincia).first()

def get_provincias(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Provincia).offset(skip).limit(limit).all()

def create_provincia(db: Session, data):
    provincia = Provincia(**data)
    db.add(provincia)
    db.commit()
    db.refresh(provincia)
    return provincia

def update_provincia(db: Session, id_provincia: int, data):
    provincia = db.query(Provincia).filter(Provincia.id_provincia == id_provincia).first()
    if not provincia:
        return None
    for key, value in data.items():
        setattr(provincia, key, value)
    db.commit()
    db.refresh(provincia)
    return provincia

def delete_provincia(db: Session, id_provincia: int):
    provincia = db.query(Provincia).filter(Provincia.id_provincia == id_provincia).first()
    if not provincia:
        return False
    db.delete(provincia)
    db.commit()
    return True
