from app.models.separador_decimal import SeparadorDecimal
from sqlalchemy.orm import Session

def get_all_separador_decimal(db: Session):
    return db.query(SeparadorDecimal).all()

def get_separador_decimal_by_id(db: Session, id: int):
    return db.query(SeparadorDecimal).filter(SeparadorDecimal.id_separador == id).first()

def create_separador_decimal(db: Session, obj):
    db_obj = SeparadorDecimal(**obj.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_separador_decimal(db: Session, db_obj, updates):
    for field, value in updates.dict().items():
        setattr(db_obj, field, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_separador_decimal(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()
