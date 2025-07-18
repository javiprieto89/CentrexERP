from app.models.tmpregistros_stock import TmpRegistroStock
from sqlalchemy.orm import Session

def get_all_tmpregistros_stock(db: Session):
    return db.query(TmpRegistroStock).all()

def get_tmpregistros_stock_by_id(db: Session, id: int):
    return db.query(TmpRegistroStock).filter(TmpRegistroStock.id_tmpRegistroStock == id).first()

def create_tmpregistro_stock(db: Session, obj):
    db_obj = TmpRegistroStock(**obj.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_tmpregistro_stock(db: Session, db_obj, updates):
    for field, value in updates.dict().items():
        setattr(db_obj, field, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_tmpregistro_stock(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()