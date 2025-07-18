from app.models.tmptransferencias import TmpTransferencia
from sqlalchemy.orm import Session

def get_all_tmptransferencias(db: Session):
    return db.query(TmpTransferencia).all()

def get_tmptransferencias_by_id(db: Session, id: int):
    return db.query(TmpTransferencia).filter(TmpTransferencia.id_tmpTransferencia == id).first()

def create_tmptransferencia(db: Session, obj):
    db_obj = TmpTransferencia(**obj.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_tmptransferencia(db: Session, db_obj, updates):
    for field, value in updates.dict().items():
        setattr(db_obj, field, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_tmptransferencia(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()