import strawberry
from app.schemas.tipos_documentos import TipoDocumentoType
from app.crud.tipos_documentos import get_all_tipos_documentos
from app.db import get_db
from typing import List

@strawberry.type
class Query:
    @strawberry.field
    def tipos_documentos(self, info) -> List[TipoDocumentoType]:
        db = next(get_db())
        return get_all_tipos_documentos(db)