from sqlalchemy.orm import Session
from app.models.marcas_items import MarcaItem

def get_marca_item(db: Session, id_marca: int):
    return db.query(MarcaItem).filter(MarcaItem.id_marca == id_marca).first()

def get_marcas_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(MarcaItem).offset(skip).limit(limit).all()

def create_marca_item(db: Session, data):
    marca = MarcaItem(**data)
    db.add(marca)
    db.commit()
    db.refresh(marca)
    return marca

def update_marca_item(db: Session, id_marca: int, data):
    marca = db.query(MarcaItem).filter(MarcaItem.id_marca == id_marca).first()
    if not marca:
        return None
    for key, value in data.items():
        setattr(marca, key, value)
    db.commit()
    db.refresh(marca)
    return marca

def delete_marca_item(db: Session, id_marca: int):
    marca = db.query(MarcaItem).filter(MarcaItem.id_marca == id_marca).first()
    if not marca:
        return False
    db.delete(marca)
    db.commit()
    return True
