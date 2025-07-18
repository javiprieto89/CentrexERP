from sqlalchemy.orm import Session
from app.models.clientes import Cliente

def get_cliente(db: Session, id_cliente: int):
    return db.query(Cliente).filter(Cliente.id_cliente == id_cliente).first()

def get_clientes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Cliente).offset(skip).limit(limit).all()

def create_cliente(db: Session, cliente_data):
    cliente = Cliente(**cliente_data)
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente

def update_cliente(db: Session, id_cliente: int, cliente_data):
    cliente = db.query(Cliente).filter(Cliente.id_cliente == id_cliente).first()
    if not cliente:
        return None
    for key, value in cliente_data.items():
        setattr(cliente, key, value)
    db.commit()
    db.refresh(cliente)
    return cliente

def delete_cliente(db: Session, id_cliente: int):
    cliente = db.query(Cliente).filter(Cliente.id_cliente == id_cliente).first()
    if not cliente:
        return False
    db.delete(cliente)
    db.commit()
    return True
