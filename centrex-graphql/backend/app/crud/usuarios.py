from app.models.usuarios import Usuario
from sqlalchemy.orm import Session

def get_all_usuarios(db: Session):
    return db.query(Usuario).all()

def get_usuarios_by_id(db: Session, id: int):
    return db.query(Usuario).filter(Usuario.id_usuario == id).first()

def create_usuario(db: Session, obj):
    db_obj = Usuario(**obj.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_usuario(db: Session, db_obj, updates):
    for field, value in updates.dict().items():
        setattr(db_obj, field, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_usuario(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()