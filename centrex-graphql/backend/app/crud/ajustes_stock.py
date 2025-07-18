from sqlalchemy.orm import Session
from app.models.ajustes_stock import AjusteStock

def get_ajuste_stock(db: Session, id_ajuste_stock: int):
    return db.query(AjusteStock).filter(AjusteStock.id_ajuste_stock == id_ajuste_stock).first()

def get_ajustes_stock(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AjusteStock).offset(skip).limit(limit).all()

def create_ajuste_stock(db: Session, data):
    ajuste = AjusteStock(**data)
    db.add(ajuste)
    db.commit()
    db.refresh(ajuste)
    return ajuste

def update_ajuste_stock(db: Session, id_ajuste_stock: int, data):
    ajuste = db.query(AjusteStock).filter(AjusteStock.id_ajuste_stock == id_ajuste_stock).first()
    if not ajuste:
        return None
    for key, value in data.items():
        setattr(ajuste, key, value)
    db.commit()
    db.refresh(ajuste)
    return ajuste

def delete_ajuste_stock(db: Session, id_ajuste_stock: int):
    ajuste = db.query(AjusteStock).filter(AjusteStock.id_ajuste_stock == id_ajuste_stock).first()
    if not ajuste:
        return False
    db.delete(ajuste)
    db.commit()
    return True
