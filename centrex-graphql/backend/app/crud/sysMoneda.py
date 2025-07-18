from app.models.sysMoneda import SysMoneda
from sqlalchemy.orm import Session

def get_all_sysMoneda(db: Session):
    return db.query(SysMoneda).all()

def get_sysMoneda_by_id(db: Session, id: int):
    return db.query(SysMoneda).filter(SysMoneda.id_moneda == id).first()

def create_sysMoneda(db: Session, obj):
    db_obj = SysMoneda(**obj.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_sysMoneda(db: Session, db_obj, updates):
    for field, value in updates.dict().items():
        setattr(db_obj, field, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_sysMoneda(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()
