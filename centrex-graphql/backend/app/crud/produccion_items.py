from sqlalchemy.orm import Session
from app.models.produccion_items import ProduccionItem

def get_produccion_item(db: Session, id_produccion_item: int):
    return db.query(ProduccionItem).filter(ProduccionItem.id_produccion_item == id_produccion_item).first()

def get_produccion_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ProduccionItem).offset(skip).limit(limit).all()

def create_produccion_item(db: Session, data):
    prod_item = ProduccionItem(**data)
    db.add(prod_item)
    db.commit()
    db.refresh(prod_item)
    return prod_item

def update_produccion_item(db: Session, id_produccion_item: int, data):
    prod_item = db.query(ProduccionItem).filter(ProduccionItem.id_produccion_item == id_produccion_item).first()
    if not prod_item:
        return None
    for key, value in data.items():
        setattr(prod_item, key, value)
    db.commit()
    db.refresh(prod_item)
    return prod_item

def delete_produccion_item(db: Session, id_produccion_item: int):
    prod_item = db.query(ProduccionItem).filter(ProduccionItem.id_produccion_item == id_produccion_item).first()
    if not prod_item:
        return False
    db.delete(prod_item)
    db.commit()
    return True
