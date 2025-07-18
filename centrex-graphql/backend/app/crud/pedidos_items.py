from sqlalchemy.orm import Session
from app.models.pedidos_items import PedidoItem

def get_pedido_item(db: Session, id_pedido_item: int):
    return db.query(PedidoItem).filter(PedidoItem.id_pedido_item == id_pedido_item).first()

def get_pedidos_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PedidoItem).offset(skip).limit(limit).all()

def create_pedido_item(db: Session, data):
    item = PedidoItem(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def update_pedido_item(db: Session, id_pedido_item: int, data):
    item = db.query(PedidoItem).filter(PedidoItem.id_pedido_item == id_pedido_item).first()
    if not item:
        return None
    for key, value in data.items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

def delete_pedido_item(db: Session, id_pedido_item: int):
    item = db.query(PedidoItem).filter(PedidoItem.id_pedido_item == id_pedido_item).first()
    if not item:
        return False
    db.delete(item)
    db.commit()
    return True
