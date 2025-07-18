from sqlalchemy.orm import Session
from app.models.cobros_retenciones import CobroRetencion

def get_cobro_retencion(db: Session, id_cobro_retencion: int):
    return db.query(CobroRetencion).filter(CobroRetencion.id_cobro_retencion == id_cobro_retencion).first()

def get_cobros_retenciones(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CobroRetencion).offset(skip).limit(limit).all()

def create_cobro_retencion(db: Session, data):
    cobro_retencion = CobroRetencion(**data)
    db.add(cobro_retencion)
    db.commit()
    db.refresh(cobro_retencion)
    return cobro_retencion

def update_cobro_retencion(db: Session, id_cobro_retencion: int, data):
    cobro_retencion = db.query(CobroRetencion).filter(CobroRetencion.id_cobro_retencion == id_cobro_retencion).first()
    if not cobro_retencion:
        return None
    for key, value in data.items():
        setattr(cobro_retencion, key, value)
    db.commit()
    db.refresh(cobro_retencion)
    return cobro_retencion

def delete_cobro_retencion(db: Session, id_cobro_retencion: int):
    cobro_retencion = db.query(CobroRetencion).filter(CobroRetencion.id_cobro_retencion == id_cobro_retencion).first()
    if not cobro_retencion:
        return False
    db.delete(cobro_retencion)
    db.commit()
    return True
