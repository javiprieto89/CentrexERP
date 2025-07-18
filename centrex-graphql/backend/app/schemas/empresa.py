import strawberry

@strawberry.type
class EmpresaType:
    id_empresa: int
    razon_social: str
    cuit: str
    direccion: str | None
    telefono: str | None
    email: str | None

@strawberry.input
class EmpresaInput:
    razon_social: str
    cuit: str
    direccion: str | None = None
    telefono: str | None = None
    email: str | None = None
