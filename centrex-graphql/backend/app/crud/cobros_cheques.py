from sqlalchemy.orm import Session
from app.models.cobros_cheques import CobroCheque

def get_cobro_cheque(db: Session, id_cobro_cheque: int):
    return db.query(CobroCheque).filter(CobroCheque.id_cobro_cheque == id_cobro_cheque).first()

def get_cobros_cheques(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CobroCheque).offset(skip).limit(limit).all()

def create_cobro_cheque(db: Session, data):
    cobro_cheque = CobroCheque(**data)
    db.add(cobro_cheque)
    db.commit()
    db.refresh(cobro_cheque)
    return cobro_cheque

def update_cobro_cheque(db: Session, id_cobro_cheque: int, data):
    cobro_cheque = db.query(CobroCheque).filter(CobroCheque.id_cobro_cheque == id_cobro_cheque).first()
    if not cobro_cheque:
        return None
    for key, value in data.items():
        setattr(cobro_cheque, key, value)
    db.commit()
    db.refresh(cobro_cheque)
    return cobro_cheque

def delete_cobro_cheque(db: Session, id_cobro_cheque: int):
    cobro_cheque = db.query(CobroCheque).filter(CobroCheque.id_cobro_cheque == id_cobro_cheque).first()
    if not cobro_cheque:
        return False
    db.delete(cobro_cheque)
    db.commit()
    return True
