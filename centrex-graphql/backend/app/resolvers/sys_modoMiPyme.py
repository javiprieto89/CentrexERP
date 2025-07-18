import strawberry
from app.schemas.sys_modoMiPyme import SysModoMiPymeType
from app.crud.sys_modoMiPyme import get_all_sysmodoMiPyme
from app.db import get_db
from typing import List

@strawberry.type
class Query:
    @strawberry.field
    def sys_modoMiPyme(self, info) -> List[SysModoMiPymeType]:
        db = next(get_db())
        return get_all_sysmodoMiPyme(db)
