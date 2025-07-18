from sqlalchemy.orm import Session
from app.models.cobros_Nfacturas_importes import CobroNFacturaImporte

def get_cobro_nfactura_importe(db: Session, id_cobro_nfactura_importe: int):
    return db.query(CobroNFacturaImporte).filter(CobroNFacturaImporte.id_cobro_nfactura_importe == id_cobro_nfactura_importe).first()

def get_cobros_nfacturas_importes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CobroNFacturaImporte).offset(skip).limit(limit).all()

def create_cobro_nfactura_importe(db: Session, data):
    cobro_nfactura_importe = CobroNFacturaImporte(**data)
    db.add(cobro_nfactura_importe)
    db.commit()
    db.refresh(cobro_nfactura_importe)
    return cobro_nfactura_importe

def update_cobro_nfactura_importe(db: Session, id_cobro_nfactura_importe: int, data):
    cobro_nfactura_importe = db.query(CobroNFacturaImporte).filter(CobroNFacturaImporte.id_cobro_nfactura_importe == id_cobro_nfactura_importe).first()
    if not cobro_nfactura_importe:
        return None
    for key, value in data.items():
        setattr(cobro_nfactura_importe, key, value)
    db.commit()
    db.refresh(cobro_nfactura_importe)
    return cobro_nfactura_importe

def delete_cobro_nfactura_importe(db: Session, id_cobro_nfactura_importe: int):
    cobro_nfactura_importe = db.query(CobroNFacturaImporte).filter(CobroNFacturaImporte.id_cobro_nfactura_importe == id_cobro_nfactura_importe).first()
    if not cobro_nfactura_importe:
        return False
    db.delete(cobro_nfactura_importe)
    db.commit()
    return True
