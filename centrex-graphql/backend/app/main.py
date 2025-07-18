"""
main.py - Entry point for the GraphQL API using Strawberry and SQLAlchemy.
"""

import strawberry
from strawberry.asgi import GraphQL
from app.db import SessionLocal, engine, Base
from app.schemas import UsuarioType
from app.models import Usuario

from app.mutations.ajustes_stock import AjustesStockMutations
from app.mutations.asocItems import AsocItemMutations
from app.mutations.bancos import BancoMutations
from app.mutations.cajas import CajaMutations
from app.mutations.cambios import CambiosMutations
from app.mutations.cc_clientes import CcClienteMutations
from app.mutations.cc_proveedores import CcProveedoreMutations
from app.mutations.cheques import ChequeMutations
from app.mutations.clientes import ClienteMutations
from app.mutations.cobros import CobroMutations
from app.mutations.cobros_cheques import CobrosChequeMutations
from app.mutations.cobros_Nfacturas_importes import CobrosNFacturasImporteMutations
from app.mutations.cobros_retenciones import CobrosRetencionMutations
from app.mutations.comprobantes import ComprobanteMutations
from app.mutations.comprobantes_compras import ComprobantesCompraMutations
from app.mutations.comprobantes_compras_conceptos import ComprobantesComprasConceptoMutations
from app.mutations.comprobantes_compras_impuestos import ComprobantesComprasImpuestoMutations
from app.mutations.comprobantes_compras_items import ComprobantesComprasItemMutations
from app.mutations.conceptos_compra import ConceptosCompraMutations
from app.mutations.condiciones_compra import CondicionesCompraMutations
from app.mutations.consultas_personalizadas import ConsultaPersonalizadaMutations
from app.mutations.cuentas_bancarias import CuentaBancariaMutations
from app.mutations.empresa import EmpresaMutations
from app.mutations.impuestos import ImpuestoMutations
from app.mutations.items import ItemMutations
from app.mutations.items_impuestos import ItemImpuestoMutations
from app.mutations.marcas_items import MarcaItemMutations
from app.mutations.ordenesCompras_items import OrdeneCompraItemMutations
from app.mutations.ordenes_compras import OrdenCompraMutations
from app.mutations.pagos import PagoMutations
from app.mutations.pagos_cheques import PagoChequeMutations
from app.mutations.pagos_nFacturas_importes import PagoNFacturaImporteMutations
from app.mutations.paises import PaisMutations
from app.mutations.pedidos import PedidoMutations
from app.mutations.pedidos_items import PedidoItemMutations
from app.mutations.perfiles import PerfilMutations
from app.mutations.permisos import PermisoMutations
from app.mutations.permisos_perfiles import PermisoPerfileMutations
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
from app.mutations.tipos_comprobantes import TipoComprobanteMutations
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
    AjustesStockMutations,
    AsocItemMutations,
    BancoMutations,
    CajaMutations,
    CambiosMutations,
    CcClienteMutations,
    CcProveedoreMutations,
    ChequeMutations,
    ClienteMutations,
    CobroMutations,
    CobrosChequeMutations,
    CobrosNFacturasImporteMutations,
    CobrosRetencionMutations,
    ComprobanteMutations,
    ComprobantesCompraMutations,
    ComprobantesComprasConceptoMutations,
    ComprobantesComprasImpuestoMutations,
    ComprobantesComprasItemMutations,
    ConceptosCompraMutations,
    CondicionesCompraMutations,
    ConsultaPersonalizadaMutations,
    CuentaBancariaMutations,
    EmpresaMutations,
    ImpuestoMutations,
    ItemMutations,
    ItemImpuestoMutations,
    MarcaItemMutations,
    OrdeneCompraItemMutations,
    OrdenCompraMutations,
    PagoMutations,
    PagoChequeMutations,
    PagoNFacturaImporteMutations,
    PaisMutations,
    PedidoMutations,
    PedidoItemMutations,
    PerfilMutations,
    PermisoMutations,
    PermisoPerfileMutations,
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
    TipoComprobanteMutations,
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
app = GraphQL(schema)

if __name__ == "__main__":
    import uvicorn
    # Crea las tablas si no existen
    Base.metadata.create_all(bind=engine)
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
