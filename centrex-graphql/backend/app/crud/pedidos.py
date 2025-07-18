from sqlalchemy.orm import Session
from app.models.pedidos import Pedido

def get_pedido(db: Session, id_pedido: int):
    return db.query(Pedido).filter(Pedido.id_pedido == id_pedido).first()

def get_pedidos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Pedido).offset(skip).limit(limit).all()

def create_pedido(db: Session, data):
    pedido = Pedido(**data)
    db.add(pedido)
    db.commit()
    db.refresh(pedido)
    return pedido

def update_pedido(db: Session, id_pedido: int, data):
    pedido = db.query(Pedido).filter(Pedido.id_pedido == id_pedido).first()
    if not pedido:
        return None
    for key, value in data.items():
        setattr(pedido, key, value)
    db.commit()
    db.refresh(pedido)
    return pedido

def delete_pedido(db: Session, id_pedido: int):
    pedido = db.query(Pedido).filter(Pedido.id_pedido == id_pedido).first()
    if not pedido:
        return False
    db.delete(pedido)
    db.commit()
    return True
