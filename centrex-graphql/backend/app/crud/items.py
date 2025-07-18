from sqlalchemy.orm import Session
from app.models.items import Item

def get_item(db: Session, id_item: int):
    return db.query(Item).filter(Item.id_item == id_item).first()

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()

def create_item(db: Session, data):
    item = Item(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def update_item(db: Session, id_item: int, data):
    item = db.query(Item).filter(Item.id_item == id_item).first()
    if not item:
        return None
    for key, value in data.items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

def delete_item(db: Session, id_item: int):
    item = db.query(Item).filter(Item.id_item == id_item).first()
    if not item:
        return False
    db.delete(item)
    db.commit()
    return True
