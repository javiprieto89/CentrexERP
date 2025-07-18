import strawberry
from typing import List, Optional
from app.schemas.ajustes_stock import AjusteStockType
from app.db import SessionLocal
from app.crud.ajustes_stock import get_ajuste_stock, get_ajustes_stock

@strawberry.type
class AjusteStockQueries:
    @strawberry.field
    def ajustes_stock(self, skip: int = 0, limit: int = 100) -> List[AjusteStockType]:
        db = SessionLocal()
        result = get_ajustes_stock(db, skip=skip, limit=limit)
        db.close()
        return [
            AjusteStockType(
                id_ajuste_stock=a.id_ajuste_stock,
                fecha=a.fecha,
                id_usuario=a.id_usuario,
                motivo=a.motivo,
                id_item=a.id_item,
                cantidad=float(a.cantidad),
                comentario=a.comentario,
                activo=a.activo
            ) for a in result
        ]

    @strawberry.field
    def ajuste_stock(self, id_ajuste_stock: int) -> Optional[AjusteStockType]:
        db = SessionLocal()
        a = get_ajuste_stock(db, id_ajuste_stock)
        db.close()
        if not a:
            return None
        return AjusteStockType(
            id_ajuste_stock=a.id_ajuste_stock,
            fecha=a.fecha,
            id_usuario=a.id_usuario,
            motivo=a.motivo,
            id_item=a.id_item,
            cantidad=float(a.cantidad),
            comentario=a.comentario,
            activo=a.activo
        )
