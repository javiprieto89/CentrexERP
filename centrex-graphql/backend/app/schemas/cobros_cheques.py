import strawberry

@strawberry.type
class CobroChequeType:
    id_cobro_cheque: int
    id_cobro: int
    id_cheque: int
    importe: float

@strawberry.input
class CobroChequeInput:
    id_cobro: int
    id_cheque: int
    importe: float
