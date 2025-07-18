from sqlalchemy.orm import Session
from app.models.cheques import Cheque

def get_cheque(db: Session, id_cheque: int):
    return db.query(Cheque).filter(Cheque.id_cheque == id_cheque).first()

def get_cheques(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Cheque).offset(skip).limit(limit).all()

def create_cheque(db: Session, data):
    cheque = Cheque(**data)
    db.add(cheque)
    db.commit()
    db.refresh(cheque)
    return cheque

def update_cheque(db: Session, id_cheque: int, data):
    cheque = db.query(Cheque).filter(Cheque.id_cheque == id_cheque).first()
    if not cheque:
        return None
    for key, value in data.items():
        setattr(cheque, key, value)
    db.commit()
    db.refresh(cheque)
    return cheque

def delete_cheque(db: Session, id_cheque: int):
    cheque = db.query(Cheque).filter(Cheque.id_cheque == id_cheque).first()
    if not cheque:
        return False
    db.delete(cheque)
    db.commit()
    return True
