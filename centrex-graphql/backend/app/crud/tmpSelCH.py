from app.models.tmpSelCH import TmpSelCH
from sqlalchemy.orm import Session

def get_all_tmpSelCH(db: Session):
    return db.query(TmpSelCH).all()

def get_tmpSelCH_by_id(db: Session, id: int):
    return db.query(TmpSelCH).filter(TmpSelCH.id_tmpSelCH == id).first()

def create_tmpSelCH(db: Session, obj):
    db_obj = TmpSelCH(**obj.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_tmpSelCH(db: Session, db_obj, updates):
    for field, value in updates.dict().items():
        setattr(db_obj, field, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_tmpSelCH(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()