from app.models.sysestados_cheques import SysEstadoCheque
from sqlalchemy.orm import Session

def get_all_sysestados_cheques(db: Session):
    return db.query(SysEstadoCheque).all()

def get_sysestados_cheques_by_id(db: Session, id: int):
    return db.query(SysEstadoCheque).filter(SysEstadoCheque.id_estadoch == id).first()

def create_sysestado_cheque(db: Session, obj):
    db_obj = SysEstadoCheque(**obj.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_sysestado_cheque(db: Session, db_obj, updates):
    for field, value in updates.dict().items():
        setattr(db_obj, field, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_sysestado_cheque(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()
