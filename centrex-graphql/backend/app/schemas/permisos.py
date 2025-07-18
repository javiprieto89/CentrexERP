import strawberry

@strawberry.type
class PermisoType:
    id_permiso: int
    nombre: str
    descripcion: str | None

@strawberry.input
class PermisoInput:
    nombre: str
    descripcion: str | None = None
