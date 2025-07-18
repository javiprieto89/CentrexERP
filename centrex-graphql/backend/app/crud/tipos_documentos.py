from app.models.tipos_documentos import TipoDocumento
from sqlalchemy.orm import Session

def get_all_tipos_documentos(db: Session):
    return db.query(TipoDocumento).all()

def get_tipos_documentos_by_id(db: Session, id: int):
    return db.query(TipoDocumento).filter(TipoDocumento.id_tipoDocumento == id).first()

def create_tipo_documento(db: Session, obj):
    db_obj = TipoDocumento(**obj.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_tipo_documento(db: Session, db_obj, updates):
    for field, value in updates.dict().items():
        setattr(db_obj, field, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_tipo_documento(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()