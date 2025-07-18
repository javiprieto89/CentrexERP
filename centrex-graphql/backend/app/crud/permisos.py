from sqlalchemy.orm import Session
from app.models.permisos import Permiso

def get_permiso(db: Session, id_permiso: int):
    return db.query(Permiso).filter(Permiso.id_permiso == id_permiso).first()

def get_permisos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Permiso).offset(skip).limit(limit).all()

def create_permiso(db: Session, data):
    permiso = Permiso(**data)
    db.add(permiso)
    db.commit()
    db.refresh(permiso)
    return permiso

def update_permiso(db: Session, id_permiso: int, data):
    permiso = db.query(Permiso).filter(Permiso.id_permiso == id_permiso).first()
    if not permiso:
        return None
    for key, value in data.items():
        setattr(permiso, key, value)
    db.commit()
    db.refresh(permiso)
    return permiso

def delete_permiso(db: Session, id_permiso: int):
    permiso = db.query(Permiso).filter(Permiso.id_permiso == id_permiso).first()
    if not permiso:
        return False
    db.delete(permiso)
    db.commit()
    return True
