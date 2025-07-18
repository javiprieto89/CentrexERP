from app.models.usuarios_perfiles import UsuarioPerfil
from sqlalchemy.orm import Session

def get_all_usuarios_perfiles(db: Session):
    return db.query(UsuarioPerfil).all()

def get_usuarios_perfiles_by_id(db: Session, id: int):
    return db.query(UsuarioPerfil).filter(UsuarioPerfil.id_usuarioPerfil == id).first()

def create_usuario_perfil(db: Session, obj):
    db_obj = UsuarioPerfil(**obj.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_usuario_perfil(db: Session, db_obj, updates):
    for field, value in updates.dict().items():
        setattr(db_obj, field, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_usuario_perfil(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()