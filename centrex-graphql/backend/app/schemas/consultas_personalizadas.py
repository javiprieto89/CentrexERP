import strawberry

@strawberry.type
class ConsultaPersonalizadaType:
    id_consulta: int
    nombre: str
    consulta_sql: str
    descripcion: str | None

@strawberry.input
class ConsultaPersonalizadaInput:
    nombre: str
    consulta_sql: str
    descripcion: str | None = None
