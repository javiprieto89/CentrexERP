import strawberry
from typing import List, Optional
from app.schemas.cobros_Nfacturas_importes import CobroNFacturaImporteType
from app.db import SessionLocal
from app.crud.cobros_Nfacturas_importes import get_cobro_nfactura_importe, get_cobros_nfacturas_importes

@strawberry.type
class CobroNFacturaImporteQueries:
    @strawberry.field
    def cobros_nfacturas_importes(self, skip: int = 0, limit: int = 100) -> List[CobroNFacturaImporteType]:
        db = SessionLocal()
        result = get_cobros_nfacturas_importes(db, skip=skip, limit=limit)
        db.close()
        return [
            CobroNFacturaImporteType(
                id_cobro_nfactura_importe=c.id_cobro_nfactura_importe,
                id_cobro=c.id_cobro,
                id_factura=c.id_factura,
                importe=float(c.importe)
            ) for c in result
        ]

    @strawberry.field
    def cobro_nfactura_importe(self, id_cobro_nfactura_importe: int) -> Optional[CobroNFacturaImporteType]:
        db = SessionLocal()
        c = get_cobro_nfactura_importe(db, id_cobro_nfactura_importe)
        db.close()
        if not c:
            return None
        return CobroNFacturaImporteType(
            id_cobro_nfactura_importe=c.id_cobro_nfactura_importe,
            id_cobro=c.id_cobro,
            id_factura=c.id_factura,
            importe=float(c.importe)
        )
