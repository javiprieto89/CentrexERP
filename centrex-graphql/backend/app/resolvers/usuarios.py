import strawberry
from app.schemas.usuarios import UsuarioType
from app.crud.usuarios import get_all_usuarios
from app.db import get_db
from typing import List

@strawberry.type
class Query:
    @strawberry.field
    def usuarios(self, info) -> List[UsuarioType]:
        db = next(get_db())
        return get_all_usuarios(db)