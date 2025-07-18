from sqlalchemy.orm import Session
from app.models.comprobantes_compras_items import ComprobanteCompraItem

def get_comprobante_compra_item(db: Session, id_item: int):
    return db.query(ComprobanteCompraItem).filter(ComprobanteCompraItem.id_item == id_item).first()

def get_comprobantes_compras_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ComprobanteCompraItem).offset(skip).limit(limit).all()

def create_comprobante_compra_item(db: Session, data):
    item = ComprobanteCompraItem(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def update_comprobante_compra_item(db: Session, id_item: int, data):
    item = db.query(ComprobanteCompraItem).filter(ComprobanteCompraItem.id_item == id_item).first()
    if not item:
        return None
    for key, value in data.items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

def delete_comprobante_compra_item(db: Session, id_item: int):
    item = db.query(ComprobanteCompraItem).filter(ComprobanteCompraItem.id_item == id_item).first()
    if not item:
        return False
    db.delete(item)
    db.commit()
    return True
