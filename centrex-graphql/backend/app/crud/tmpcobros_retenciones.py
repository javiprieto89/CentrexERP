from app.models.tmpcobros_retenciones import TmpCobroRetencion
from sqlalchemy.orm import Session

def get_all_tmpcobros_retenciones(db: Session):
    return db.query(TmpCobroRetencion).all()

def get_tmpcobros_retenciones_by_id(db: Session, id: int):
    return db.query(TmpCobroRetencion).filter(TmpCobroRetencion.id_tmpCobroRetencion == id).first()

def get_tmpcobro_retencion_by_id(db: Session, id: int):
    """Return a single TmpCobroRetencion by its primary key."""
    return db.query(TmpCobroRetencion).filter(TmpCobroRetencion.id_tmpCobroRetencion == id).first()

def create_tmpcobro_retencion(db: Session, obj):
    db_obj = TmpCobroRetencion(**obj.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_tmpcobro_retencion(db: Session, db_obj, updates):
    for field, value in updates.dict().items():
        setattr(db_obj, field, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_tmpcobro_retencion(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()