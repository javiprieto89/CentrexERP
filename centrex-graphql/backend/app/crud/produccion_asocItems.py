from sqlalchemy.orm import Session
from app.models.produccion_asocItems import ProduccionAsocItem

def get_produccion_asoc_item(db: Session, id_asoc: int):
    return db.query(ProduccionAsocItem).filter(ProduccionAsocItem.id_asoc == id_asoc).first()

def get_produccion_asoc_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ProduccionAsocItem).offset(skip).limit(limit).all()

def create_produccion_asoc_item(db: Session, data):
    asoc = ProduccionAsocItem(**data)
    db.add(asoc)
    db.commit()
    db.refresh(asoc)
    return asoc

def update_produccion_asoc_item(db: Session, id_asoc: int, data):
    asoc = db.query(ProduccionAsocItem).filter(ProduccionAsocItem.id_asoc == id_asoc).first()
    if not asoc:
        return None
    for key, value in data.items():
        setattr(asoc, key, value)
    db.commit()
    db.refresh(asoc)
    return asoc

def delete_produccion_asoc_item(db: Session, id_asoc: int):
    asoc = db.query(ProduccionAsocItem).filter(ProduccionAsocItem.id_asoc == id_asoc).first()
    if not asoc:
        return False
    db.delete(asoc)
    db.commit()
    return True
