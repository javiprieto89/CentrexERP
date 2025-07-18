from sqlalchemy.orm import Session
from app.models.comprobantes_compras import ComprobanteCompra

def get_comprobante_compra(db: Session, id_comprobante_compra: int):
    return db.query(ComprobanteCompra).filter(ComprobanteCompra.id_comprobante_compra == id_comprobante_compra).first()

def get_comprobantes_compras(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ComprobanteCompra).offset(skip).limit(limit).all()

def create_comprobante_compra(db: Session, data):
    comprobante = ComprobanteCompra(**data)
    db.add(comprobante)
    db.commit()
    db.refresh(comprobante)
    return comprobante

def update_comprobante_compra(db: Session, id_comprobante_compra: int, data):
    comprobante = db.query(ComprobanteCompra).filter(ComprobanteCompra.id_comprobante_compra == id_comprobante_compra).first()
    if not comprobante:
        return None
    for key, value in data.items():
        setattr(comprobante, key, value)
    db.commit()
    db.refresh(comprobante)
    return comprobante

def delete_comprobante_compra(db: Session, id_comprobante_compra: int):
    comprobante = db.query(ComprobanteCompra).filter(ComprobanteCompra.id_comprobante_compra == id_comprobante_compra).first()
    if not comprobante:
        return False
    db.delete(comprobante)
    db.commit()
    return True
