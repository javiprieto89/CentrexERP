import strawberry
from typing import Optional
from app.schemas.tipos_documentos import TipoDocumentoType, TipoDocumentoInput
from app.db import SessionLocal
from app.crud.tipos_documentos import create_tipo_documento, update_tipo_documento, delete_tipo_documento

@strawberry.type
class TipoDocumentoMutations:
    @strawberry.mutation
    def create_tipo_documento(self, data: TipoDocumentoInput) -> TipoDocumentoType:
        db = SessionLocal()
        new_obj = create_tipo_documento(db, data.__dict__)
        db.close()
        return TipoDocumentoType(**new_obj.__dict__)

    @strawberry.mutation
    def update_tipo_documento(self, id_tipoDocumento: int, data: TipoDocumentoInput) -> Optional[TipoDocumentoType]:
        db = SessionLocal()
        updated = update_tipo_documento(db, id_tipoDocumento, data.__dict__)
        db.close()
        if not updated:
            return None
        return TipoDocumentoType(**updated.__dict__)

    @strawberry.mutation
    def delete_tipo_documento(self, id_tipoDocumento: int) -> bool:
        db = SessionLocal()
        result = delete_tipo_documento(db, id_tipoDocumento)
        db.close()
        return result