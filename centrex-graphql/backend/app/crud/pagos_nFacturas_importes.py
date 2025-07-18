from sqlalchemy.orm import Session
from app.models.pagos_nFacturas_importes import PagoNFacturaImporte

def get_pago_nfactura_importe(db: Session, id_pago_factura: int):
    return db.query(PagoNFacturaImporte).filter(PagoNFacturaImporte.id_pago_factura == id_pago_factura).first()

def get_pagos_nfacturas_importes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PagoNFacturaImporte).offset(skip).limit(limit).all()

def create_pago_nfactura_importe(db: Session, data):
    pago = PagoNFacturaImporte(**data)
    db.add(pago)
    db.commit()
    db.refresh(pago)
    return pago

def update_pago_nfactura_importe(db: Session, id_pago_factura: int, data):
    pago = db.query(PagoNFacturaImporte).filter(PagoNFacturaImporte.id_pago_factura == id_pago_factura).first()
    if not pago:
        return None
    for key, value in data.items():
        setattr(pago, key, value)
    db.commit()
    db.refresh(pago)
    return pago

def delete_pago_nfactura_importe(db: Session, id_pago_factura: int):
    pago = db.query(PagoNFacturaImporte).filter(PagoNFacturaImporte.id_pago_factura == id_pago_factura).first()
    if not pago:
        return False
    db.delete(pago)
    db.commit()
    return True
