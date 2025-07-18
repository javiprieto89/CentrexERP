import strawberry

@strawberry.type
class BancoType:
    id_banco: int
    nombre: str
    activo: bool

@strawberry.input
class BancoInput:
    nombre: str
    activo: bool = True
