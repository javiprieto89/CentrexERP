import strawberry
from typing import Optional

@strawberry.type
class TiposComprobantesType:
    id_tipoComprobante: int
    comprobante_AFIP: str
    id_claseFiscal: int
    signoProveedor: str
    signoCliente: str
    discriminaIVA: bool
    esRemito: bool
    nombreAbreviado: str
    id_claseComprobante: int
    id_anulaTipoComprobante: Optional[int]
    contabilizar: bool

@strawberry.input
class TiposComprobantesInput:
    comprobante_AFIP: str
    id_claseFiscal: int
    signoProveedor: str
    signoCliente: str
    discriminaIVA: bool
    esRemito: bool
    nombreAbreviado: str
    id_claseComprobante: int
    id_anulaTipoComprobante: Optional[int] = None
    contabilizar: bool = True