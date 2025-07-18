from sqlalchemy.orm import Session
from app.models.empresa import Empresa

def get_empresa(db: Session, id_empresa: int):
    return db.query(Empresa).filter(Empresa.id_empresa == id_empresa).first()

def get_empresas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Empresa).offset(skip).limit(limit).all()

def create_empresa(db: Session, data):
    empresa = Empresa(**data)
    db.add(empresa)
    db.commit()
    db.refresh(empresa)
    return empresa

def update_empresa(db: Session, id_empresa: int, data):
    empresa = db.query(Empresa).filter(Empresa.id_empresa == id_empresa).first()
    if not empresa:
        return None
    for key, value in data.items():
        setattr(empresa, key, value)
    db.commit()
    db.refresh(empresa)
    return empresa

def delete_empresa(db: Session, id_empresa: int):
    empresa = db.query(Empresa).filter(Empresa.id_empresa == id_empresa).first()
    if not empresa:
        return False
    db.delete(empresa)
    db.commit()
    return True
