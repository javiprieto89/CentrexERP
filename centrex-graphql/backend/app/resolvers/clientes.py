import strawberry
from typing import List, Optional
from app.schemas.clientes import ClienteType
from app.db import SessionLocal
from app.crud.clientes import get_cliente, get_clientes

@strawberry.type
class ClienteQueries:
    @strawberry.field
    def clientes(self, skip: int = 0, limit: int = 100) -> List[ClienteType]:
        db = SessionLocal()
        result = get_clientes(db, skip=skip, limit=limit)
        db.close()
        return [
            ClienteType(
                id_cliente=c.id_cliente,
                taxNumber=c.taxNumber,
                razon_social=c.razon_social,
                nombre_fantasia=c.nombre_fantasia,
                contacto=c.contacto,
                telefono=c.telefono,
                celular=c.celular,
                email=c.email,
                id_provincia_fiscal=c.id_provincia_fiscal,
                direccion_fiscal=c.direccion_fiscal,
                localidad_fiscal=c.localidad_fiscal,
                cp_fiscal=c.cp_fiscal,
                id_provincia_entrega=c.id_provincia_entrega,
                direccion_entrega=c.direccion_entrega,
                localidad_entrega=c.localidad_entrega,
                cp_entrega=c.cp_entrega,
                notas=c.notas,
                esInscripto=c.esInscripto,
                activo=c.activo,
                id_tipoDocumento=c.id_tipoDocumento,
                id_claseFiscal=c.id_claseFiscal
            ) for c in result
        ]

    @strawberry.field
    def cliente(self, id_cliente: int) -> Optional[ClienteType]:
        db = SessionLocal()
        c = get_cliente(db, id_cliente)
        db.close()
        if not c:
            return None
        return ClienteType(
            id_cliente=c.id_cliente,
            taxNumber=c.taxNumber,
            razon_social=c.razon_social,
            nombre_fantasia=c.nombre_fantasia,
            contacto=c.contacto,
            telefono=c.telefono,
            celular=c.celular,
            email=c.email,
            id_provincia_fiscal=c.id_provincia_fiscal,
            direccion_fiscal=c.direccion_fiscal,
            localidad_fiscal=c.localidad_fiscal,
            cp_fiscal=c.cp_fiscal,
            id_provincia_entrega=c.id_provincia_entrega,
            direccion_entrega=c.direccion_entrega,
            localidad_entrega=c.localidad_entrega,
            cp_entrega=c.cp_entrega,
            notas=c.notas,
            esInscripto=c.esInscripto,
            activo=c.activo,
            id_tipoDocumento=c.id_tipoDocumento,
            id_claseFiscal=c.id_claseFiscal
        )
