from sqlalchemy.orm import Session
from app.models.conceptos_compra import ConceptoCompra

def get_concepto_compra(db: Session, id_concepto: int):
    return db.query(ConceptoCompra).filter(ConceptoCompra.id_concepto == id_concepto).first()

def get_conceptos_compra(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ConceptoCompra).offset(skip).limit(limit).all()

def create_concepto_compra(db: Session, data):
    concepto = ConceptoCompra(**data)
    db.add(concepto)
    db.commit()
    db.refresh(concepto)
    return concepto

def update_concepto_compra(db: Session, id_concepto: int, data):
    concepto = db.query(ConceptoCompra).filter(ConceptoCompra.id_concepto == id_concepto).first()
    if not concepto:
        return None
    for key, value in data.items():
        setattr(concepto, key, value)
    db.commit()
    db.refresh(concepto)
    return concepto

def delete_concepto_compra(db: Session, id_concepto: int):
    concepto = db.query(ConceptoCompra).filter(ConceptoCompra.id_concepto == id_concepto).first()
    if not concepto:
        return False
    db.delete(concepto)
    db.commit()
    return True
