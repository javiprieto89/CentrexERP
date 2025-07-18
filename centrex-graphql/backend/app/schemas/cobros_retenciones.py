import strawberry

@strawberry.type
class CobroRetencionType:
    id_cobro_retencion: int
    id_cobro: int
    tipo_retencion: str
    importe: float

@strawberry.input
class CobroRetencionInput:
    id_cobro: int
    tipo_retencion: str
    importe: float
