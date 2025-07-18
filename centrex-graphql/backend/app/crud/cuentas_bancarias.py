from sqlalchemy.orm import Session
from app.models.cuentas_bancarias import CuentaBancaria

def get_cuenta_bancaria(db: Session, id_cuenta: int):
    return db.query(CuentaBancaria).filter(CuentaBancaria.id_cuenta == id_cuenta).first()

def get_cuentas_bancarias(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CuentaBancaria).offset(skip).limit(limit).all()

def create_cuenta_bancaria(db: Session, data):
    cuenta = CuentaBancaria(**data)
    db.add(cuenta)
    db.commit()
    db.refresh(cuenta)
    return cuenta

def update_cuenta_bancaria(db: Session, id_cuenta: int, data):
    cuenta = db.query(CuentaBancaria).filter(CuentaBancaria.id_cuenta == id_cuenta).first()
    if not cuenta:
        return None
    for key, value in data.items():
        setattr(cuenta, key, value)
    db.commit()
    db.refresh(cuenta)
    return cuenta

def delete_cuenta_bancaria(db: Session, id_cuenta: int):
    cuenta = db.query(CuentaBancaria).filter(CuentaBancaria.id_cuenta == id_cuenta).first()
    if not cuenta:
        return False
    db.delete(cuenta)
    db.commit()
    return True
