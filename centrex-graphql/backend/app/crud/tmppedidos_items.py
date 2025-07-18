from app.models.tmppedidos_items import TmpPedidoItem
from sqlalchemy.orm import Session

def get_all_tmppedidos_items(db: Session):
    return db.query(TmpPedidoItem).all()

def get_tmppedidos_items_by_id(db: Session, id: int):
    return db.query(TmpPedidoItem).filter(TmpPedidoItem.id_tmpPedidoItem == id).first()

def create_tmppedido_item(db: Session, obj):
    db_obj = TmpPedidoItem(**obj.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_tmppedido_item(db: Session, db_obj, updates):
    for field, value in updates.dict().items():
        setattr(db_obj, field, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_tmppedido_item(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()