import strawberry

@strawberry.type
class CuentaBancariaType:
    id_cuenta: int
    banco: str
    sucursal: str | None
    numero: str
    titular: str
    cbu: str | None
    saldo: float

@strawberry.input
class CuentaBancariaInput:
    banco: str
    sucursal: str | None = None
    numero: str
    titular: str
    cbu: str | None = None
    saldo: float = 0
