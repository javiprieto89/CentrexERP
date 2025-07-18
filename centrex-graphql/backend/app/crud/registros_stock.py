from app.models.registros_stock import RegistroStock
from sqlalchemy.orm import Session

def get_all_registros_stock(db: Session):
    return db.query(RegistroStock).all()

def get_registros_stock_by_id(db: Session, id: int):
    return db.query(RegistroStock).filter(RegistroStock.id_registro == id).first()

def create_registro_stock(db: Session, obj):
    db_obj = RegistroStock(**obj.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_registro_stock(db: Session, db_obj, updates):
    for field, value in updates.dict().items():
        setattr(db_obj, field, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_registro_stock(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()
