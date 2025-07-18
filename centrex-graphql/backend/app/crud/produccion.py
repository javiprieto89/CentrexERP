from sqlalchemy.orm import Session
from app.models.produccion import Produccion

def get_produccion(db: Session, id_produccion: int):
    return db.query(Produccion).filter(Produccion.id_produccion == id_produccion).first()

def get_producciones(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Produccion).offset(skip).limit(limit).all()

def create_produccion(db: Session, data):
    produccion = Produccion(**data)
    db.add(produccion)
    db.commit()
    db.refresh(produccion)
    return produccion

def update_produccion(db: Session, id_produccion: int, data):
    produccion = db.query(Produccion).filter(Produccion.id_produccion == id_produccion).first()
    if not produccion:
        return None
    for key, value in data.items():
        setattr(produccion, key, value)
    db.commit()
    db.refresh(produccion)
    return produccion

def delete_produccion(db: Session, id_produccion: int):
    produccion = db.query(Produccion).filter(Produccion.id_produccion == id_produccion).first()
    if not produccion:
        return False
    db.delete(produccion)
    db.commit()
    return True
