from app.models.tmpproduccion_items import TmpProduccionItem
from sqlalchemy.orm import Session

__all__ = [
    "get_all_tmpproduccion_items",
    "get_tmpproduccion_items_by_id",
    "get_tmpproduccion_item_by_id",
    "create_tmpproduccion_item",
    "update_tmpproduccion_item",
    "delete_tmpproduccion_item",
]

def get_all_tmpproduccion_items(db: Session):
    return db.query(TmpProduccionItem).all()

def get_tmpproduccion_items_by_id(db: Session, id: int):
    return db.query(TmpProduccionItem).filter(TmpProduccionItem.id_tmpProduccionItem == id).first()

def get_tmpproduccion_item_by_id(db: Session, id: int):
    """Return a single TmpProduccionItem by its primary key."""
    return db.query(TmpProduccionItem).filter(TmpProduccionItem.id_tmpProduccionItem == id).first()

def create_tmpproduccion_item(db: Session, obj):
    db_obj = TmpProduccionItem(**obj.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_tmpproduccion_item(db: Session, db_obj, updates):
    for field, value in updates.dict().items():
        setattr(db_obj, field, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_tmpproduccion_item(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()

