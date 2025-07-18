import strawberry

@strawberry.type
class PerfilType:
    id_perfil: int
    nombre: str
    descripcion: str | None

@strawberry.input
class PerfilInput:
    nombre: str
    descripcion: str | None = None
