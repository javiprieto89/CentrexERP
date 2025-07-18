from sqlalchemy.orm import Session
from app.models.cc_clientes import CcCliente

def get_cc_cliente(db: Session, id_cc_cliente: int):
    return db.query(CcCliente).filter(CcCliente.id_cc_cliente == id_cc_cliente).first()

def get_cc_clientes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CcCliente).offset(skip).limit(limit).all()

def create_cc_cliente(db: Session, data):
    cc_cliente = CcCliente(**data)
    db.add(cc_cliente)
    db.commit()
    db.refresh(cc_cliente)
    return cc_cliente

def update_cc_cliente(db: Session, id_cc_cliente: int, data):
    cc_cliente = db.query(CcCliente).filter(CcCliente.id_cc_cliente == id_cc_cliente).first()
    if not cc_cliente:
        return None
    for key, value in data.items():
        setattr(cc_cliente, key, value)
    db.commit()
    db.refresh(cc_cliente)
    return cc_cliente

def delete_cc_cliente(db: Session, id_cc_cliente: int):
    cc_cliente = db.query(CcCliente).filter(CcCliente.id_cc_cliente == id_cc_cliente).first()
    if not cc_cliente:
        return False
    db.delete(cc_cliente)
    db.commit()
    return True
