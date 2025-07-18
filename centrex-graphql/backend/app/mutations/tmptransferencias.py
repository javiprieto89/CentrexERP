import strawberry
from typing import Optional
from app.schemas.tmptransferencias import TmpTransferenciaType, TmpTransferenciaInput
from app.db import SessionLocal
from app.crud.tmptransferencias import create_tmptransferencia, update_tmptransferencia, delete_tmptransferencia

@strawberry.type
class TmpTransferenciaMutations:
    @strawberry.mutation
    def create_tmp_transferencia(self, data: TmpTransferenciaInput) -> TmpTransferenciaType:
        db = SessionLocal()
        new_obj = create_tmptransferencia(db, data.__dict__)
        db.close()
        return TmpTransferenciaType(**new_obj.__dict__)

    @strawberry.mutation
    def update_tmp_transferencia(self, id_tmpTransferencia: int, data: TmpTransferenciaInput) -> Optional[TmpTransferenciaType]:
        db = SessionLocal()
        updated = update_tmptransferencia(db, id_tmpTransferencia, data.__dict__)
        db.close()
        if not updated:
            return None
        return TmpTransferenciaType(**updated.__dict__)

    @strawberry.mutation
    def delete_tmp_transferencia(self, id_tmpTransferencia: int) -> bool:
        db = SessionLocal()
        result = delete_tmptransferencia(db, id_tmpTransferencia)
        db.close()
        return result