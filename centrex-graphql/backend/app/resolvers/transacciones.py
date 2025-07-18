import strawberry
from app.schemas.transacciones import TransaccionType
from app.crud.transacciones import get_all_transacciones
from app.db import get_db
from typing import List

@strawberry.type
class Query:
    @strawberry.field
    def transacciones(self, info) -> List[TransaccionType]:
        db = next(get_db())
        return get_all_transacciones(db)