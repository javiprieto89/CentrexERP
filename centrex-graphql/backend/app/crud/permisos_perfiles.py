from sqlalchemy.orm import Session
from app.models.permisos_perfiles import PermisoPerfil

def get_permiso_perfil(db: Session, id_permiso_perfil: int):
    return db.query(PermisoPerfil).filter(PermisoPerfil.id_permiso_perfil == id_permiso_perfil).first()

def get_permisos_perfiles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PermisoPerfil).offset(skip).limit(limit).all()

def create_permiso_perfil(db: Session, data):
    permiso = PermisoPerfil(**data)
    db.add(permiso)
    db.commit()
    db.refresh(permiso)
    return permiso

def update_permiso_perfil(db: Session, id_permiso_perfil: int, data):
    permiso = db.query(PermisoPerfil).filter(PermisoPerfil.id_permiso_perfil == id_permiso_perfil).first()
    if not permiso:
        return None
    for key, value in data.items():
        setattr(permiso, key, value)
    db.commit()
    db.refresh(permiso)
    return permiso

def delete_permiso_perfil(db: Session, id_permiso_perfil: int):
    permiso = db.query(PermisoPerfil).filter(PermisoPerfil.id_permiso_perfil == id_permiso_perfil).first()
    if not permiso:
        return False
    db.delete(permiso)
    db.commit()
    return True
