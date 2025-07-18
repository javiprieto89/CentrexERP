import strawberry

@strawberry.type
class ConceptoCompraType:
    id_concepto: int
    descripcion: str

@strawberry.input
class ConceptoCompraInput:
    descripcion: str
