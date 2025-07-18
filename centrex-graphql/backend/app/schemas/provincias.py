import strawberry

@strawberry.type
class ProvinciaType:
    id_provincia: int
    nombre: str
    id_pais: int

@strawberry.input
class ProvinciaInput:
    nombre: str
    id_pais: int
