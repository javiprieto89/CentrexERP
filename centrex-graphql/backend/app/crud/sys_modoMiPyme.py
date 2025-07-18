from app.models.sys_modoMiPyme import SysModoMiPyme
from sqlalchemy.orm import Session

def get_all_sysmodoMiPyme(db: Session):
    return db.query(SysModoMiPyme).all()

def get_sysmodoMiPyme_by_id(db: Session, id: int):
    return db.query(SysModoMiPyme).filter(SysModoMiPyme.id_modoMiPyme == id).first()

def create_sysmodoMiPyme(db: Session, obj):
    db_obj = SysModoMiPyme(**obj.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_sysmodoMiPyme(db: Session, db_obj, updates):
    for field, value in updates.dict().items():
        setattr(db_obj, field, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_sysmodoMiPyme(db: Session, id_modoMiPyme: int) -> bool:
    obj = db.query(SysModoMiPyme).filter(SysModoMiPyme.id_modoMiPyme == id_modoMiPyme).first()
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True
