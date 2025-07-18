from app.models.sys_claseComprobante import SysClaseComprobante
from sqlalchemy.orm import Session

def get_all_sysclaseComprobante(db: Session):
    return db.query(SysClaseComprobante).all()

def get_sysclaseComprobante_by_id(db: Session, id: int):
    return db.query(SysClaseComprobante).filter(SysClaseComprobante.id_claseComprobante == id).first()

def create_sysclaseComprobante(db: Session, obj):
    db_obj = SysClaseComprobante(**obj.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_sysclaseComprobante(db: Session, db_obj, updates):
    for field, value in updates.dict().items():
        setattr(db_obj, field, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_sysclaseComprobante(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()
