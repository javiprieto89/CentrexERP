"""
main.py - Entry point for the GraphQL API using Strawberry and SQLAlchemy.
"""

import strawberry
from strawberry.asgi import GraphQL
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from app.db import SessionLocal, engine, Base
from app.schemas import UsuarioType
from app.models import Usuario

from app.mutations.ajustes_stock import AjusteStockMutations
from app.mutations.asocItems import AsocItemMutations
from app.mutations.bancos import BancoMutations
from app.mutations.cajas import CajaMutations
from app.mutations.cambios import CambioMutations
from app.mutations.cc_clientes import CCClienteMutations
from app.mutations.cc_proveedores import CCProveedorMutations
from app.mutations.cheques import ChequeMutations
from app.mutations.clientes import ClienteMutations
from app.mutations.cobros import CobroMutations
from app.mutations.cobros_cheques import CobroChequeMutations
from app.mutations.cobros_Nfacturas_importes import CobroNFacturaImporteMutations
from app.mutations.cobros_retenciones import CobroRetencionMutations
from app.mutations.comprobantes import ComprobanteMutations
from app.mutations.comprobantes_compras import ComprobanteCompraMutations
from app.mutations.comprobantes_compras_conceptos import ComprobanteCompraConceptoMutations
from app.mutations.comprobantes_compras_impuestos import ComprobanteCompraImpuestoMutations
from app.mutations.comprobantes_compras_items import ComprobanteCompraItemMutations
from app.mutations.conceptos_compra import ConceptoCompraMutations
from app.mutations.condiciones_compra import CondicionCompraMutations
from app.mutations.consultas_personalizadas import ConsultaPersonalizadaMutations
from app.mutations.cuentas_bancarias import CuentaBancariaMutations
from app.mutations.empresa import EmpresaMutations
from app.mutations.impuestos import ImpuestoMutations
from app.mutations.items import ItemMutations
from app.mutations.items_impuestos import ItemImpuestoMutations
from app.mutations.marcas_items import MarcaItemMutations
from app.mutations.ordenesCompras_items import OrdenCompraItemMutations
from app.mutations.ordenes_compras import OrdenCompraMutations
from app.mutations.pagos import PagoMutations
from app.mutations.pagos_cheques import PagoChequeMutations
from app.mutations.pagos_nFacturas_importes import PagoNFacturaImporteMutations
from app.mutations.paises import PaisMutations
from app.mutations.pedidos import PedidoMutations
from app.mutations.pedidos_items import PedidoItemMutations
from app.mutations.perfiles import PerfilMutations
from app.mutations.permisos import PermisoMutations
from app.mutations.permisos_perfiles import PermisoPerfilMutations
from app.mutations.produccion import ProduccionMutations
from app.mutations.produccion_asocItems import ProduccionAsocItemMutations
from app.mutations.produccion_items import ProduccionItemMutations
from app.mutations.proveedores import ProveedorMutations
from app.mutations.provincias import ProvinciaMutations
from app.mutations.registros_stock import RegistroStockMutations
from app.mutations.separador_decimal import SeparadorDecimalMutations
from app.mutations.sysestados_cheques import SysEstadoChequeMutations
from app.mutations.sysMoneda import SysMonedaMutations
from app.mutations.sys_claseComprobante import SysClaseComprobanteMutations
from app.mutations.sys_ClasesFiscales import SysClaseFiscalMutations
from app.mutations.sys_modoMiPyme import SysModoMiPymeMutations
from app.mutations.tipos_comprobantes import TiposComprobantesMutations
from app.mutations.tipos_documentos import TipoDocumentoMutations
from app.mutations.tipos_items import TipoItemMutations
from app.mutations.tmpcobros_retenciones import TmpCobroRetencionMutations
from app.mutations.tmpOC_items import TmpOCItemMutations
from app.mutations.tmppedidos_items import TmpPedidoItemMutations
from app.mutations.tmpproduccion_asocItems import TmpProduccionAsocItemMutations
from app.mutations.tmpproduccion_items import TmpProduccionItemMutations
from app.mutations.tmpregistros_stock import TmpRegistroStockMutations
from app.mutations.tmpSelCH import TmpSelCHMutations
from app.mutations.tmptransferencias import TmpTransferenciaMutations
from app.mutations.transacciones import TransaccionMutations
from app.mutations.transferencias import TransferenciaMutations
from app.mutations.usuarios import UsuarioMutations
from app.mutations.usuarios_perfiles import UsuarioPerfilMutations

def get_db():
    """Session generator for SQLAlchemy."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "¡Hola, GraphQL!"

    @strawberry.field
    def usuarios(self, info) -> list[UsuarioType]:
        db = next(get_db())
        usuarios = db.query(Usuario).all()
        return [
            UsuarioType(
                id_usuario=u.id_usuario,
                usuario=u.usuario,
                nombre=u.nombre,
                activo=u.activo,
                logueado=u.logueado
            ) for u in usuarios
        ]

@strawberry.type
class Mutation(
    AjusteStockMutations,
    AsocItemMutations,
    BancoMutations,
    CajaMutations,
    CambioMutations,
    CCClienteMutations,
    CCProveedorMutations,
    ChequeMutations,
    ClienteMutations,
    CobroMutations,
    CobroChequeMutations,
    CobroNFacturaImporteMutations,
    CobroRetencionMutations,
    ComprobanteMutations,
    ComprobanteCompraMutations,
    ComprobanteCompraConceptoMutations,
    ComprobanteCompraImpuestoMutations,
    ComprobanteCompraItemMutations,
    ConceptoCompraMutations,
    CondicionCompraMutations,
    ConsultaPersonalizadaMutations,
    CuentaBancariaMutations,
    EmpresaMutations,
    ImpuestoMutations,
    ItemMutations,
    ItemImpuestoMutations,
    MarcaItemMutations,
    OrdenCompraItemMutations,
    OrdenCompraMutations,
    PagoMutations,
    PagoChequeMutations,
    PagoNFacturaImporteMutations,
    PaisMutations,
    PedidoMutations,
    PedidoItemMutations,
    PerfilMutations,
    PermisoMutations,
    PermisoPerfilMutations,
    ProduccionMutations,
    ProduccionAsocItemMutations,
    ProduccionItemMutations,
    ProveedorMutations,
    ProvinciaMutations,
    RegistroStockMutations,
    SeparadorDecimalMutations,
    SysEstadoChequeMutations,
    SysMonedaMutations,
    SysClaseComprobanteMutations,
    SysClaseFiscalMutations,
    SysModoMiPymeMutations,
    TiposComprobantesMutations,
    TipoDocumentoMutations,
    TipoItemMutations,
    TmpCobroRetencionMutations,
    TmpOCItemMutations,
    TmpPedidoItemMutations,
    TmpProduccionAsocItemMutations,
    TmpProduccionItemMutations,
    TmpRegistroStockMutations,
    TmpSelCHMutations,
    TmpTransferenciaMutations,
    TransaccionMutations,
    TransferenciaMutations,
    UsuarioMutations,
    UsuarioPerfilMutations
):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQL(schema)

# Starlette app with CORS enabled and GraphQL mounted at /graphql
app = Starlette()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/graphql", graphql_app)

if __name__ == "__main__":
    import uvicorn
    # Crea las tablas si no existen
    Base.metadata.create_all(bind=engine)
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
