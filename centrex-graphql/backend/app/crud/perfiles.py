from sqlalchemy.orm import Session
from app.models.perfiles import Perfil

def get_perfil(db: Session, id_perfil: int):
    return db.query(Perfil).filter(Perfil.id_perfil == id_perfil).first()

def get_perfiles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Perfil).offset(skip).limit(limit).all()

def create_perfil(db: Session, data):
    perfil = Perfil(**data)
    db.add(perfil)
    db.commit()
    db.refresh(perfil)
    return perfil

def update_perfil(db: Session, id_perfil: int, data):
    perfil = db.query(Perfil).filter(Perfil.id_perfil == id_perfil).first()
    if not perfil:
        return None
    for key, value in data.items():
        setattr(perfil, key, value)
    db.commit()
    db.refresh(perfil)
    return perfil

def delete_perfil(db: Session, id_perfil: int):
    perfil = db.query(Perfil).filter(Perfil.id_perfil == id_perfil).first()
    if not perfil:
        return False
    db.delete(perfil)
    db.commit()
    return True
