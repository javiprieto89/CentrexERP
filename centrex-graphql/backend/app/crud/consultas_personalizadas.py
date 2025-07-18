from sqlalchemy.orm import Session
from app.models.consultas_personalizadas import ConsultaPersonalizada

def get_consulta_personalizada(db: Session, id_consulta: int):
    return db.query(ConsultaPersonalizada).filter(ConsultaPersonalizada.id_consulta == id_consulta).first()

def get_consultas_personalizadas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ConsultaPersonalizada).offset(skip).limit(limit).all()

def create_consulta_personalizada(db: Session, data):
    consulta = ConsultaPersonalizada(**data)
    db.add(consulta)
    db.commit()
    db.refresh(consulta)
    return consulta

def update_consulta_personalizada(db: Session, id_consulta: int, data):
    consulta = db.query(ConsultaPersonalizada).filter(ConsultaPersonalizada.id_consulta == id_consulta).first()
    if not consulta:
        return None
    for key, value in data.items():
        setattr(consulta, key, value)
    db.commit()
    db.refresh(consulta)
    return consulta

def delete_consulta_personalizada(db: Session, id_consulta: int):
    consulta = db.query(ConsultaPersonalizada).filter(ConsultaPersonalizada.id_consulta == id_consulta).first()
    if not consulta:
        return False
    db.delete(consulta)
    db.commit()
    return True
