# === CONFIGURACION INICIAL ===
$basePath = "centrex-graphql\backend\app"

# Lista de entidades sacadas del script.sql (NO incluir la tabla 'clients')
$entities = @(
    "ajustes_stock", "asocItems", "bancos", "cajas", "cambios", "cc_clientes", "cc_proveedores", "cheques",
    "clientes", "cobros", "cobros_cheques", "cobros_Nfacturas_importes", "cobros_retenciones",
    "comprobantes", "comprobantes_compras", "comprobantes_compras_conceptos", "comprobantes_compras_impuestos",
    "comprobantes_compras_items", "conceptos_compra", "condiciones_compra", "consultas_personalizadas",
    "cuentas_bancarias", "empresa", "impuestos", "items", "items_impuestos", "marcas_items", "ordenes_compras",
    "ordenesCompras_items", "paises", "pagos", "pagos_cheques", "pagos_nFacturas_importes", "pedidos",
    "pedidos_items", "perfiles", "permisos", "permisos_perfiles", "produccion", "produccion_asocItems",
    "produccion_items", "proveedores", "provincias", "registros_stock", "separador_decimal",
    "sys_claseComprobante", "sys_ClasesFiscales", "sys_modoMiPyme", "sysestados_cheques", "sysMoneda",
    "tipos_comprobantes", "tipos_documentos", "tipos_items", "user"
)

# Carpeta de cada módulo
$folders = @(
    "$basePath\models",
    "$basePath\schemas",
    "$basePath\resolvers",
    "$basePath\mutations",
    "$basePath\crud"
)

# Crear carpetas
foreach ($folder in $folders) {
    New-Item -ItemType Directory -Force -Path $folder | Out-Null
}

# Archivos para cada entidad en cada carpeta
foreach ($entity in $entities) {
    foreach ($folder in $folders) {
        $file = "$folder\$entity.py"
        if (!(Test-Path $file)) {
            New-Item -ItemType File -Path $file | Out-Null
        }
    }
}

# Crear __init__.py en cada carpeta si no existe
foreach ($folder in $folders) {
    $file = "$folder\__init__.py"
    if (!(Test-Path $file)) {
        New-Item -ItemType File -Path $file | Out-Null
    }
}

# Crear archivo de conexión DB
$dbfile = "$basePath\db.py"
if (!(Test-Path $dbfile)) {
    New-Item -ItemType File -Path $dbfile | Out-Null
}

Write-Host "¡Estructura y archivos base generados! Incluyendo carpeta crud para cada entidad."
