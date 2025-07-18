from app.models.transacciones import Transaccion
from sqlalchemy.orm import Session

def get_all_transacciones(db: Session):
    return db.query(Transaccion).all()

def get_transacciones_by_id(db: Session, id: int):
    return db.query(Transaccion).filter(Transaccion.id_transaccion == id).first()

def create_transaccion(db: Session, obj):
    db_obj = Transaccion(**obj.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_transaccion(db: Session, db_obj, updates):
    for field, value in updates.dict().items():
        setattr(db_obj, field, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_transaccion(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()