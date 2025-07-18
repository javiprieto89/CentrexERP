from app.models.sys_ClasesFiscales import SysClaseFiscal
from sqlalchemy.orm import Session

def get_all_sysClasesFiscales(db: Session):
    return db.query(SysClaseFiscal).all()

def get_sysClasesFiscales_by_id(db: Session, id: int):
    return db.query(SysClaseFiscal).filter(SysClaseFiscal.id_claseFiscal == id).first()

def create_sysClasesFiscales(db: Session, obj):
    db_obj = SysClaseFiscal(**obj.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_sysClasesFiscales(db: Session, db_obj, updates):
    for field, value in updates.dict().items():
        setattr(db_obj, field, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_sysClasesFiscales(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()
