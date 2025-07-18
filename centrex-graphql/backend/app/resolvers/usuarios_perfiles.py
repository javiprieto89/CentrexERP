import strawberry
from app.schemas.usuarios_perfiles import UsuarioPerfilType
from app.crud.usuarios_perfiles import get_all_usuarios_perfiles
from app.db import get_db
from typing import List

@strawberry.type
class Query:
    @strawberry.field
    def usuarios_perfiles(self, info) -> List[UsuarioPerfilType]:
        db = next(get_db())
        return get_all_usuarios_perfiles(db)