from sqlalchemy.orm import Session
from app.models.cobros import Cobro

def get_cobro(db: Session, id_cobro: int):
    return db.query(Cobro).filter(Cobro.id_cobro == id_cobro).first()

def get_cobros(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Cobro).offset(skip).limit(limit).all()

def create_cobro(db: Session, data):
    cobro = Cobro(**data)
    db.add(cobro)
    db.commit()
    db.refresh(cobro)
    return cobro

def update_cobro(db: Session, id_cobro: int, data):
    cobro = db.query(Cobro).filter(Cobro.id_cobro == id_cobro).first()
    if not cobro:
        return None
    for key, value in data.items():
        setattr(cobro, key, value)
    db.commit()
    db.refresh(cobro)
    return cobro

def delete_cobro(db: Session, id_cobro: int):
    cobro = db.query(Cobro).filter(Cobro.id_cobro == id_cobro).first()
    if not cobro:
        return False
    db.delete(cobro)
    db.commit()
    return True
