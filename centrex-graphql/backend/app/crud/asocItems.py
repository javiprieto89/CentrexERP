from sqlalchemy.orm import Session
from app.models.asocItems import AsocItem

def get_asocitem(db: Session, id_asocItem: int):
    return db.query(AsocItem).filter(AsocItem.id_asocItem == id_asocItem).first()

def get_asocitems(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AsocItem).offset(skip).limit(limit).all()

def create_asocitem(db: Session, data):
    asocitem = AsocItem(**data)
    db.add(asocitem)
    db.commit()
    db.refresh(asocitem)
    return asocitem

def update_asocitem(db: Session, id_asocItem: int, data):
    asocitem = db.query(AsocItem).filter(AsocItem.id_asocItem == id_asocItem).first()
    if not asocitem:
        return None
    for key, value in data.items():
        setattr(asocitem, key, value)
    db.commit()
    db.refresh(asocitem)
    return asocitem

def delete_asocitem(db: Session, id_asocItem: int):
    asocitem = db.query(AsocItem).filter(AsocItem.id_asocItem == id_asocItem).first()
    if not asocitem:
        return False
    db.delete(asocitem)
    db.commit()
    return True
