from sqlalchemy.orm import Session
from app.models.impuestos import Impuesto

def get_impuesto(db: Session, id_impuesto: int):
    return db.query(Impuesto).filter(Impuesto.id_impuesto == id_impuesto).first()

def get_impuestos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Impuesto).offset(skip).limit(limit).all()

def create_impuesto(db: Session, data):
    impuesto = Impuesto(**data)
    db.add(impuesto)
    db.commit()
    db.refresh(impuesto)
    return impuesto

def update_impuesto(db: Session, id_impuesto: int, data):
    impuesto = db.query(Impuesto).filter(Impuesto.id_impuesto == id_impuesto).first()
    if not impuesto:
        return None
    for key, value in data.items():
        setattr(impuesto, key, value)
    db.commit()
    db.refresh(impuesto)
    return impuesto

def delete_impuesto(db: Session, id_impuesto: int):
    impuesto = db.query(Impuesto).filter(Impuesto.id_impuesto == id_impuesto).first()
    if not impuesto:
        return False
    db.delete(impuesto)
    db.commit()
    return True
