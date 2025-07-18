from sqlalchemy.orm import Session
from app.models.condiciones_compra import CondicionCompra

def get_condicion_compra(db: Session, id_condicion: int):
    return db.query(CondicionCompra).filter(CondicionCompra.id_condicion == id_condicion).first()

def get_condiciones_compra(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CondicionCompra).offset(skip).limit(limit).all()

def create_condicion_compra(db: Session, data):
    condicion = CondicionCompra(**data)
    db.add(condicion)
    db.commit()
    db.refresh(condicion)
    return condicion

def update_condicion_compra(db: Session, id_condicion: int, data):
    condicion = db.query(CondicionCompra).filter(CondicionCompra.id_condicion == id_condicion).first()
    if not condicion:
        return None
    for key, value in data.items():
        setattr(condicion, key, value)
    db.commit()
    db.refresh(condicion)
    return condicion

def delete_condicion_compra(db: Session, id_condicion: int):
    condicion = db.query(CondicionCompra).filter(CondicionCompra.id_condicion == id_condicion).first()
    if not condicion:
        return False
    db.delete(condicion)
    db.commit()
    return True
