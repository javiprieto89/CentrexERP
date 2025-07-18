import strawberry
from typing import Optional
from app.schemas.pagos_nFacturas_importes import PagoNFacturaImporteType, PagoNFacturaImporteInput
from app.db import SessionLocal
from app.crud.pagos_nFacturas_importes import create_pago_nfactura_importe, update_pago_nfactura_importe, delete_pago_nfactura_importe

@strawberry.type
class PagoNFacturaImporteMutations:
    @strawberry.mutation
    def create_pago_nfactura_importe(self, data: PagoNFacturaImporteInput) -> PagoNFacturaImporteType:
        db = SessionLocal()
        new_obj = create_pago_nfactura_importe(db, data.__dict__)
        db.close()
        return PagoNFacturaImporteType(**new_obj.__dict__)

    @strawberry.mutation
    def update_pago_nfactura_importe(self, id_pago_factura: int, data: PagoNFacturaImporteInput) -> Optional[PagoNFacturaImporteType]:
        db = SessionLocal()
        updated = update_pago_nfactura_importe(db, id_pago_factura, data.__dict__)
        db.close()
        if not updated:
            return None
        return PagoNFacturaImporteType(**updated.__dict__)

    @strawberry.mutation
    def delete_pago_nfactura_importe(self, id_pago_factura: int) -> bool:
        db = SessionLocal()
        result = delete_pago_nfactura_importe(db, id_pago_factura)
        db.close()
        return result
