
$modelsPath = "backend/models"
$relationshipMap = @{
    "id_provincia_fiscal" = @{ ref="provincias"; class="Provincias" }
    "id_provincia_entrega" = @{ ref="provincias"; class="Provincias" }
    "id_tipoDocumento" = @{ ref="tipos_documentos"; class="TiposDocumentos" }
    "id_claseFiscal" = @{ ref="sys_ClasesFiscales"; class="SysClasesFiscales" }
    "id_usuario" = @{ ref="usuarios"; class="Usuarios" }
    "id_perfil" = @{ ref="perfiles"; class="Perfiles" }
    "id_moneda" = @{ ref="sysMoneda"; class="SysMoneda" }
    "id_cliente" = @{ ref="clientes"; class="Clientes" }
    "id_proveedor" = @{ ref="proveedores"; class="Proveedores" }
    "id_item" = @{ ref="items"; class="Items" }
    "id_cuenta_bancaria" = @{ ref="cuentas_bancarias"; class="CuentasBancarias" }
    "id_impuesto" = @{ ref="impuestos"; class="Impuestos" }
}

Get-ChildItem -Path $modelsPath -Filter *.py | ForEach-Object {
    $path = $_.FullName
    $file = Get-Content $path
    Copy-Item $path "$path.bak"

    $modified = $false
    $newLines = @()

    foreach ($line in $file) {
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

    # Agregar relaciones al final si no existen aún
    foreach ($key in $relationshipMap.Keys) {
        $relLine = "    " + $key.Trim("id_") + " = relationship(`"" + $relationshipMap[$key].class + "`", lazy=`"joined`")"
        if (-not ($file -join "`n" -match [regex]::Escape($relLine))) {
            $newLines += $relLine
            $modified = $true
        }
    }

    if ($modified) {
        Set-Content -Path $path -Value $newLines
        Write-Host "Modificado: $path"
    }
}
