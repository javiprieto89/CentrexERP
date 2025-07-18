import strawberry

@strawberry.type
class CajaType:
    id_caja: int
    nombre: str
    saldo_inicial: float | None
    activo: bool

@strawberry.input
class CajaInput:
    nombre: str
    saldo_inicial: float | None = None
    activo: bool = True
