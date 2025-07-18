import strawberry
from app.schemas.tmpSelCH import TmpSelCHType
from app.crud.tmpSelCH import get_all_tmpSelCH
from app.db import get_db
from typing import List

@strawberry.type
class Query:
    @strawberry.field
    def tmpSelCH(self, info) -> List[TmpSelCHType]:
        db = next(get_db())
        return get_all_tmpSelCH(db)