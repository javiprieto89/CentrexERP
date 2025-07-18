import strawberry
from app.schemas.transferencias import TransferenciaType
from app.crud.transferencias import get_all_transferencias
from app.db import get_db
from typing import List

@strawberry.type
class Query:
    @strawberry.field
    def transferencias(self, info) -> List[TransferenciaType]:
        db = next(get_db())
        return get_all_transferencias(db)