import strawberry
from typing import Optional
from app.schemas.consultas_personalizadas import ConsultaPersonalizadaType, ConsultaPersonalizadaInput
from app.db import SessionLocal
from app.crud.consultas_personalizadas import create_consulta_personalizada, update_consulta_personalizada, delete_consulta_personalizada

@strawberry.type
class ConsultaPersonalizadaMutations:
    @strawberry.mutation
    def create_consulta_personalizada(self, data: ConsultaPersonalizadaInput) -> ConsultaPersonalizadaType:
        db = SessionLocal()
        new_obj = create_consulta_personalizada(db, data.__dict__)
        db.close()
        return ConsultaPersonalizadaType(**new_obj.__dict__)

    @strawberry.mutation
    def update_consulta_personalizada(self, id_consulta: int, data: ConsultaPersonalizadaInput) -> Optional[ConsultaPersonalizadaType]:
        db = SessionLocal()
        updated = update_consulta_personalizada(db, id_consulta, data.__dict__)
        db.close()
        if not updated:
            return None
        return ConsultaPersonalizadaType(**updated.__dict__)

    @strawberry.mutation
    def delete_consulta_personalizada(self, id_consulta: int) -> bool:
        db = SessionLocal()
        result = delete_consulta_personalizada(db, id_consulta)
        db.close()
        return result
