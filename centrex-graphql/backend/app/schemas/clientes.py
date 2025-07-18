import strawberry

@strawberry.type
class ClienteType:
    id_cliente: int
    taxNumber: str | None
    razon_social: str
    nombre_fantasia: str | None
    contacto: str | None
    telefono: str | None
    celular: str | None
    email: str | None
    id_provincia_fiscal: int | None
    direccion_fiscal: str | None
    localidad_fiscal: str | None
    cp_fiscal: str | None
    id_provincia_entrega: int | None
    direccion_entrega: str | None
    localidad_entrega: str | None
    cp_entrega: str | None
    notas: str | None
    esInscripto: bool
    activo: bool
    id_tipoDocumento: int
    id_claseFiscal: int | None

@strawberry.input
class ClienteInput:
    taxNumber: str | None = None
    razon_social: str
    nombre_fantasia: str | None = None
    contacto: str | None = None
    telefono: str | None = None
    celular: str | None = None
    email: str | None = None
    id_provincia_fiscal: int | None = None
    direccion_fiscal: str | None = None
    localidad_fiscal: str | None = None
    cp_fiscal: str | None = None
    id_provincia_entrega: int | None = None
    direccion_entrega: str | None = None
    localidad_entrega: str | None = None
    cp_entrega: str | None = None
    notas: str | None = None
    esInscripto: bool = False
    activo: bool = True
    id_tipoDocumento: int
    id_claseFiscal: int | None = None
