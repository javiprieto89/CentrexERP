import strawberry
from typing import Optional
from app.schemas.cobros_Nfacturas_importes import CobroNFacturaImporteType, CobroNFacturaImporteInput
from app.db import SessionLocal
from app.crud.cobros_Nfacturas_importes import create_cobro_nfactura_importe, update_cobro_nfactura_importe, delete_cobro_nfactura_importe

@strawberry.type
class CobroNFacturaImporteMutations:
    @strawberry.mutation
    def create_cobro_nfactura_importe(self, data: CobroNFacturaImporteInput) -> CobroNFacturaImporteType:
        db = SessionLocal()
        new_item = create_cobro_nfactura_importe(db, data.__dict__)
        db.close()
        return CobroNFacturaImporteType(**new_item.__dict__)

    @strawberry.mutation
    def update_cobro_nfactura_importe(self, id_cobro_nfactura_importe: int, data: CobroNFacturaImporteInput) -> Optional[CobroNFacturaImporteType]:
        db = SessionLocal()
        updated = update_cobro_nfactura_importe(db, id_cobro_nfactura_importe, data.__dict__)
        db.close()
        if not updated:
            return None
        return CobroNFacturaImporteType(**updated.__dict__)

    @strawberry.mutation
    def delete_cobro_nfactura_importe(self, id_cobro_nfactura_importe: int) -> bool:
        db = SessionLocal()
        result = delete_cobro_nfactura_importe(db, id_cobro_nfactura_importe)
        db.close()
        return result
