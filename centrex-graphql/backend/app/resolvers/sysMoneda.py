import strawberry
from app.schemas.sysMoneda import SysMonedaType
from app.crud.sysMoneda import get_all_sysMoneda
from app.db import get_db
from typing import List

@strawberry.type
class Query:
    @strawberry.field
    def sysMoneda(self, info) -> List[SysMonedaType]:
        db = next(get_db())
        return get_all_sysMoneda(db)
