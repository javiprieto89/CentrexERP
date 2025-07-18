from app.models.tmpOC_items import TmpOCItem
from sqlalchemy.orm import Session

def get_all_tmpOC_items(db: Session):
    return db.query(TmpOCItem).all()

def get_tmpOC_items_by_id(db: Session, id: int):
    return db.query(TmpOCItem).filter(TmpOCItem.id_tmpOCItem == id).first()

def create_tmpOC_item(db: Session, obj):
    db_obj = TmpOCItem(**obj.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_tmpOC_item(db: Session, db_obj, updates):
    for field, value in updates.dict().items():
        setattr(db_obj, field, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_tmpOC_item(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()