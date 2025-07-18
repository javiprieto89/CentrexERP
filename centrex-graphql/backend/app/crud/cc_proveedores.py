from sqlalchemy.orm import Session
from app.models.cc_proveedores import CcProveedor

def get_cc_proveedor(db: Session, id_cc_proveedor: int):
    return db.query(CcProveedor).filter(CcProveedor.id_cc_proveedor == id_cc_proveedor).first()

def get_cc_proveedores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CcProveedor).offset(skip).limit(limit).all()

def create_cc_proveedor(db: Session, data):
    cc_proveedor = CcProveedor(**data)
    db.add(cc_proveedor)
    db.commit()
    db.refresh(cc_proveedor)
    return cc_proveedor

def update_cc_proveedor(db: Session, id_cc_proveedor: int, data):
    cc_proveedor = db.query(CcProveedor).filter(CcProveedor.id_cc_proveedor == id_cc_proveedor).first()
    if not cc_proveedor:
        return None
    for key, value in data.items():
        setattr(cc_proveedor, key, value)
    db.commit()
    db.refresh(cc_proveedor)
    return cc_proveedor

def delete_cc_proveedor(db: Session, id_cc_proveedor: int):
    cc_proveedor = db.query(CcProveedor).filter(CcProveedor.id_cc_proveedor == id_cc_proveedor).first()
    if not cc_proveedor:
        return False
    db.delete(cc_proveedor)
    db.commit()
    return True
