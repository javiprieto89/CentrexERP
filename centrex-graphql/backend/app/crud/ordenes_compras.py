from sqlalchemy.orm import Session
from app.models.ordenes_compras import OrdenCompra

def get_orden_compra(db: Session, id_orden: int):
    return db.query(OrdenCompra).filter(OrdenCompra.id_orden == id_orden).first()

def get_ordenes_compras(db: Session, skip: int = 0, limit: int = 100):
    return db.query(OrdenCompra).offset(skip).limit(limit).all()

def create_orden_compra(db: Session, data):
    orden = OrdenCompra(**data)
    db.add(orden)
    db.commit()
    db.refresh(orden)
    return orden

def update_orden_compra(db: Session, id_orden: int, data):
    orden = db.query(OrdenCompra).filter(OrdenCompra.id_orden == id_orden).first()
    if not orden:
        return None
    for key, value in data.items():
        setattr(orden, key, value)
    db.commit()
    db.refresh(orden)
    return orden

def delete_orden_compra(db: Session, id_orden: int):
    orden = db.query(OrdenCompra).filter(OrdenCompra.id_orden == id_orden).first()
    if not orden:
        return False
    db.delete(orden)
    db.commit()
    return True
