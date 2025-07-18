from app.models.tmpproduccion_asocItems import TmpProduccionAsocItem
from sqlalchemy.orm import Session

def get_all_tmpproduccion_asocItems(db: Session):
    return db.query(TmpProduccionAsocItem).all()

def get_tmpproduccion_asocItems_by_id(db: Session, id: int):
    return db.query(TmpProduccionAsocItem).filter(TmpProduccionAsocItem.id_tmpProduccionAsocItem == id).first()

def create_tmpproduccion_asocItem(db: Session, obj):
    db_obj = TmpProduccionAsocItem(**obj.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_tmpproduccion_asocItem(db: Session, db_obj, updates):
    for field, value in updates.dict().items():
        setattr(db_obj, field, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_tmpproduccion_asocItem(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()