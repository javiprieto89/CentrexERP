import strawberry
from typing import List, Optional
from app.schemas.consultas_personalizadas import ConsultaPersonalizadaType
from app.db import SessionLocal
from app.crud.consultas_personalizadas import get_consulta_personalizada, get_consultas_personalizadas

@strawberry.type
class ConsultaPersonalizadaQueries:
    @strawberry.field
    def consultas_personalizadas(self, skip: int = 0, limit: int = 100) -> List[ConsultaPersonalizadaType]:
        db = SessionLocal()
        result = get_consultas_personalizadas(db, skip=skip, limit=limit)
        db.close()
        return [
            ConsultaPersonalizadaType(
                id_consulta=c.id_consulta,
                nombre=c.nombre,
                consulta_sql=c.consulta_sql,
                descripcion=c.descripcion
            ) for c in result
        ]

    @strawberry.field
    def consulta_personalizada(self, id_consulta: int) -> Optional[ConsultaPersonalizadaType]:
        db = SessionLocal()
        c = get_consulta_personalizada(db, id_consulta)
        db.close()
        if not c:
            return None
        return ConsultaPersonalizadaType(
            id_consulta=c.id_consulta,
            nombre=c.nombre,
            consulta_sql=c.consulta_sql,
            descripcion=c.descripcion
        )
