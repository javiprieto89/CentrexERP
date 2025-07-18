from sqlalchemy.orm import Session
from app.models.comprobantes_compras_impuestos import ComprobanteCompraImpuesto

def get_comprobante_compra_impuesto(db: Session, id_impuesto: int):
    return db.query(ComprobanteCompraImpuesto).filter(ComprobanteCompraImpuesto.id_impuesto == id_impuesto).first()

def get_comprobantes_compras_impuestos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ComprobanteCompraImpuesto).offset(skip).limit(limit).all()

def create_comprobante_compra_impuesto(db: Session, data):
    impuesto = ComprobanteCompraImpuesto(**data)
    db.add(impuesto)
    db.commit()
    db.refresh(impuesto)
    return impuesto

def update_comprobante_compra_impuesto(db: Session, id_impuesto: int, data):
    impuesto = db.query(ComprobanteCompraImpuesto).filter(ComprobanteCompraImpuesto.id_impuesto == id_impuesto).first()
    if not impuesto:
        return None
    for key, value in data.items():
        setattr(impuesto, key, value)
    db.commit()
    db.refresh(impuesto)
    return impuesto

def delete_comprobante_compra_impuesto(db: Session, id_impuesto: int):
    impuesto = db.query(ComprobanteCompraImpuesto).filter(ComprobanteCompraImpuesto.id_impuesto == id_impuesto).first()
    if not impuesto:
        return False
    db.delete(impuesto)
    db.commit()
    return True
