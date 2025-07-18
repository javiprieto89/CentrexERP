
$modelsPath = "backend/app/models"
$relationshipMap = @{
    "id_item" = @{ ref="items"; class="Items" }
    "id_item_asoc" = @{ ref="items"; class="Items" }
    "id_pais" = @{ ref="paises"; class="Paises" }
    "id_cliente" = @{ ref="clientes"; class="Clientes" }
    "id_moneda" = @{ ref="sysMoneda"; class="Sysmoneda" }
    "id_proveedor" = @{ ref="proveedores"; class="Proveedores" }
    "id_banco" = @{ ref="bancos"; class="Bancos" }
    "id_cuentaBancaria" = @{ ref="cuentas_bancarias"; class="CuentasBancarias" }
    "id_estadoch" = @{ ref="sysestados_cheques"; class="SysestadosCheques" }
    "id_provincia_fiscal" = @{ ref="provincias"; class="Provincias" }
    "id_provincia_entrega" = @{ ref="provincias"; class="Provincias" }
    "id_claseFiscal" = @{ ref="sys_ClasesFiscales"; class="SysClasesfiscales" }
    "id_tipoDocumento" = @{ ref="tipos_documentos"; class="TiposDocumentos" }
    "id_cheque" = @{ ref="cheques"; class="Cheques" }
    "id_cobro" = @{ ref="cobros"; class="Cobros" }
    "id_impuesto" = @{ ref="impuestos"; class="Impuestos" }
    "id_modoMiPyme" = @{ ref="sys_modoMiPyme"; class="SysModomipyme" }
    "id_tipoComprobante" = @{ ref="tipos_comprobantes"; class="TiposComprobantes" }
    "id_cc" = @{ ref="cc_proveedores"; class="CcProveedores" }
    "id_condicion_compra" = @{ ref="condiciones_compra"; class="CondicionesCompra" }
    "id_comprobanteCompra" = @{ ref="comprobantes_compras"; class="ComprobantesCompras" }
    "id_concepto_compra" = @{ ref="conceptos_compra"; class="ConceptosCompra" }
    "id_marca" = @{ ref="marcas_items"; class="MarcasItems" }
    "id_tipo" = @{ ref="tipos_items"; class="TiposItems" }
    "id_ordenCompra" = @{ ref="ordenes_compras"; class="OrdenesCompras" }
    "id_pago" = @{ ref="pagos"; class="Pagos" }
    "id_cc], [id_cliente" = @{ ref="cc_clientes"; class="CcClientes" }
    "id_comprobante" = @{ ref="comprobantes"; class="Comprobantes" }
    "id_usuario" = @{ ref="usuarios"; class="Usuarios" }
    "id_pedido" = @{ ref="pedidos"; class="Pedidos" }
    "id_pefil" = @{ ref="perfiles"; class="Perfiles" }
    "id_permiso" = @{ ref="permisos"; class="Permisos" }
    "id_item], [id_item_asoc" = @{ ref="asocItems"; class="Asocitems" }
    "id_produccion" = @{ ref="produccion"; class="Produccion" }
    "id_item_recibido" = @{ ref="items"; class="Items" }
    "id_claseComprobante" = @{ ref="sys_claseComprobante"; class="SysClasecomprobante" }
    "id_ocItem" = @{ ref="ordenesCompras_items"; class="OrdenescomprasItems" }
    "id_pedidoItem" = @{ ref="pedidos_items"; class="PedidosItems" }
    "id_produccionItem" = @{ ref="produccion_items"; class="ProduccionItems" }
    "id_tmpProduccionItem" = @{ ref="tmpproduccion_items"; class="TmpproduccionItems" }
    "id_perfil" = @{ ref="perfiles"; class="Perfiles" }
}


Get-ChildItem -Path $modelsPath -Filter *.py | ForEach-Object {
    $path = $_.FullName
    $fileContent = Get-Content $path -Raw
    Copy-Item $path "$path.bak"

    $lines = $fileContent -split "`n"
    $newLines = @()
    $modified = $false

    foreach ($line in $lines) {
        $newLine = $line
        foreach ($key in $relationshipMap.Keys) {
            if ($line -match "^\s*$key\s*=" -and $line -notmatch "ForeignKey") {
                $fkTarget = $relationshipMap[$key].ref
                $newLine = $newLine -replace "Column\(([^)]*)\)", "Column(`$1, ForeignKey(`"$fkTarget.id`"))"
                $modified = $true
            }
        }
        $newLines += $newLine
    }

    $classBlock = $newLines -join "`n"
    foreach ($key in $relationshipMap.Keys) {
        $relName = $key -replace "^id_", ""
        $className = $relationshipMap[$key].class
        $relLine = "    $relName = relationship(`"$className`", lazy=`"joined`")"
        if ($classBlock -notmatch [regex]::Escape($relLine)) {
            $newLines += $relLine
            $modified = $true
        }
    }

    if ($modified) {
        Set-Content -Path $path -Value $newLines
        Write-Host "Modificado: $path"
    }
}
