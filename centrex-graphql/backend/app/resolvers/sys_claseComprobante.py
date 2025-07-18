import strawberry
from app.schemas.sys_claseComprobante import SysClaseComprobanteType
from app.crud.sys_claseComprobante import get_all_sysclaseComprobante
from app.db import get_db
from typing import List

@strawberry.type
class Query:
    @strawberry.field
    def sys_claseComprobante(self, info) -> List[SysClaseComprobanteType]:
        db = next(get_db())
        return get_all_sysclaseComprobante(db)
