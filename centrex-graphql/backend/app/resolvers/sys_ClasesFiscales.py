import strawberry
from app.schemas.sys_ClasesFiscales import SysClaseFiscalType
from app.crud.sys_ClasesFiscales import get_all_sysClasesFiscales
from app.db import get_db
from typing import List

@strawberry.type
class Query:
    @strawberry.field
    def sys_ClasesFiscales(self, info) -> List[SysClaseFiscalType]:
        db = next(get_db())
        return get_all_sysClasesFiscales(db)
