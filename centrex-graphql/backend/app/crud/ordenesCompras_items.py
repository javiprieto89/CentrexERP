from sqlalchemy.orm import Session
from app.models.ordenesCompras_items import OrdenCompraItem

def get_orden_compra_item(db: Session, id_orden_item: int):
    return db.query(OrdenCompraItem).filter(OrdenCompraItem.id_orden_item == id_orden_item).first()

def get_ordenes_compras_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(OrdenCompraItem).offset(skip).limit(limit).all()

def create_orden_compra_item(db: Session, data):
    item = OrdenCompraItem(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def update_orden_compra_item(db: Session, id_orden_item: int, data):
    item = db.query(OrdenCompraItem).filter(OrdenCompraItem.id_orden_item == id_orden_item).first()
    if not item:
        return None
    for key, value in data.items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

def delete_orden_compra_item(db: Session, id_orden_item: int):
    item = db.query(OrdenCompraItem).filter(OrdenCompraItem.id_orden_item == id_orden_item).first()
    if not item:
        return False
    db.delete(item)
    db.commit()
    return True
