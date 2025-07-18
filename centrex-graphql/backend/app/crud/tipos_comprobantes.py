from app.models.tipos_comprobantes import TipoComprobante
from sqlalchemy.orm import Session

def get_all_tipos_comprobantes(db: Session):
    return db.query(TipoComprobante).all()

def get_tipos_comprobantes_by_id(db: Session, id: int):
    return db.query(TipoComprobante).filter(TipoComprobante.id_tipoComprobante == id).first()

def create_tipo_comprobante(db: Session, obj):
    db_obj = TipoComprobante(**obj.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_tipo_comprobante(db: Session, db_obj, updates):
    for field, value in updates.dict().items():
        setattr(db_obj, field, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_tipo_comprobante(db: Session, id_tipoComprobante: int) -> bool:
    obj = db.query(TipoComprobante).filter(TipoComprobante.id_tipoComprobante == id_tipoComprobante).first()
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True
