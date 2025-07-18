from app.models.tipos_items import TipoItem
from sqlalchemy.orm import Session

def get_all_tipos_items(db: Session):
    return db.query(TipoItem).all()

def get_tipos_items_by_id(db: Session, id: int):
    return db.query(TipoItem).filter(TipoItem.id_tipoItem == id).first()

def create_tipo_item(db: Session, obj):
    db_obj = TipoItem(**obj.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_tipo_item(db: Session, db_obj, updates):
    for field, value in updates.dict().items():
        setattr(db_obj, field, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_tipo_item(db: Session, id_tipoItem: int) -> bool:
    obj = db.query(TipoItem).filter(TipoItem.id_tipoItem == id_tipoItem).first()
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True