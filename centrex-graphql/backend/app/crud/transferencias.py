from app.models.transferencias import Transferencia
from sqlalchemy.orm import Session

def get_all_transferencias(db: Session):
    return db.query(Transferencia).all()

def get_transferencias_by_id(db: Session, id: int):
    return db.query(Transferencia).filter(Transferencia.id_transferencia == id).first()

def create_transferencia(db: Session, obj):
    db_obj = Transferencia(**obj.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_transferencia(db: Session, db_obj, updates):
    for field, value in updates.dict().items():
        setattr(db_obj, field, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_transferencia(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()