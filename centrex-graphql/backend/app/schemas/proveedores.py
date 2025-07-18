import strawberry

@strawberry.type
class ProveedorType:
    id_proveedor: int
    nombre: str
    direccion: str | None
    telefono: str | None
    email: str | None

@strawberry.input
class ProveedorInput:
    nombre: str
    direccion: str | None = None
    telefono: str | None = None
    email: str | None = None
