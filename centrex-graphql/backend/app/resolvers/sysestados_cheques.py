import strawberry
from app.schemas.sysestados_cheques import SysEstadoChequeType
from app.crud.sysestados_cheques import get_all_sysestados_cheques
from app.db import get_db
from typing import List

@strawberry.type
class Query:
    @strawberry.field
    def sysestados_cheques(self, info) -> List[SysEstadoChequeType]:
        db = next(get_db())
        return get_all_sysestados_cheques(db)
