from sqlalchemy.orm import Session
from app.models.bancos import Banco

def get_banco(db: Session, id_banco: int):
    return db.query(Banco).filter(Banco.id_banco == id_banco).first()

def get_bancos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Banco).offset(skip).limit(limit).all()

def create_banco(db: Session, data):
    banco = Banco(**data)
    db.add(banco)
    db.commit()
    db.refresh(banco)
    return banco

def update_banco(db: Session, id_banco: int, data):
    banco = db.query(Banco).filter(Banco.id_banco == id_banco).first()
    if not banco:
        return None
    for key, value in data.items():
        setattr(banco, key, value)
    db.commit()
    db.refresh(banco)
    return banco

def delete_banco(db: Session, id_banco: int):
    banco = db.query(Banco).filter(Banco.id_banco == id_banco).first()
    if not banco:
        return False
    db.delete(banco)
    db.commit()
    return True
