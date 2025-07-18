from sqlalchemy.orm import Session
from app.models.proveedores import Proveedor

def get_proveedor(db: Session, id_proveedor: int):
    return db.query(Proveedor).filter(Proveedor.id_proveedor == id_proveedor).first()

def get_proveedores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Proveedor).offset(skip).limit(limit).all()

def create_proveedor(db: Session, data):
    prov = Proveedor(**data)
    db.add(prov)
    db.commit()
    db.refresh(prov)
    return prov

def update_proveedor(db: Session, id_proveedor: int, data):
    prov = db.query(Proveedor).filter(Proveedor.id_proveedor == id_proveedor).first()
    if not prov:
        return None
    for key, value in data.items():
        setattr(prov, key, value)
    db.commit()
    db.refresh(prov)
    return prov

def delete_proveedor(db: Session, id_proveedor: int):
    prov = db.query(Proveedor).filter(Proveedor.id_proveedor == id_proveedor).first()
    if not prov:
        return False
    db.delete(prov)
    db.commit()
    return True
