from sqlalchemy.orm import Session
from app.models.items_impuestos import ItemImpuesto

def get_item_impuesto(db: Session, id_item_impuesto: int):
    return db.query(ItemImpuesto).filter(ItemImpuesto.id_item_impuesto == id_item_impuesto).first()

def get_items_impuestos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ItemImpuesto).offset(skip).limit(limit).all()

def create_item_impuesto(db: Session, data):
    item = ItemImpuesto(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def update_item_impuesto(db: Session, id_item_impuesto: int, data):
    item = db.query(ItemImpuesto).filter(ItemImpuesto.id_item_impuesto == id_item_impuesto).first()
    if not item:
        return None
    for key, value in data.items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

def delete_item_impuesto(db: Session, id_item_impuesto: int):
    item = db.query(ItemImpuesto).filter(ItemImpuesto.id_item_impuesto == id_item_impuesto).first()
    if not item:
        return False
    db.delete(item)
    db.commit()
    return True
