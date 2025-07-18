from sqlalchemy.orm import Session
from app.models.comprobantes_compras_conceptos import ComprobanteCompraConcepto

def get_comprobante_compra_concepto(db: Session, id_concepto: int):
    return db.query(ComprobanteCompraConcepto).filter(ComprobanteCompraConcepto.id_concepto == id_concepto).first()

def get_comprobantes_compras_conceptos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ComprobanteCompraConcepto).offset(skip).limit(limit).all()

def create_comprobante_compra_concepto(db: Session, data):
    concepto = ComprobanteCompraConcepto(**data)
    db.add(concepto)
    db.commit()
    db.refresh(concepto)
    return concepto

def update_comprobante_compra_concepto(db: Session, id_concepto: int, data):
    concepto = db.query(ComprobanteCompraConcepto).filter(ComprobanteCompraConcepto.id_concepto == id_concepto).first()
    if not concepto:
        return None
    for key, value in data.items():
        setattr(concepto, key, value)
    db.commit()
    db.refresh(concepto)
    return concepto

def delete_comprobante_compra_concepto(db: Session, id_concepto: int):
    concepto = db.query(ComprobanteCompraConcepto).filter(ComprobanteCompraConcepto.id_concepto == id_concepto).first()
    if not concepto:
        return False
    db.delete(concepto)
    db.commit()
    return True
