# Builds the CurseForge-importable modpack zip into build/
$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot

# Fetch Modrinth-only embedded jars (not committed to git; CC0/GPL-licensed)
$dagJar = Join-Path $root 'overrides/mods/dagmod-1.10.0.jar'
if (-not (Test-Path $dagJar)) {
    New-Item -ItemType Directory -Force (Join-Path $root 'overrides/mods') | Out-Null
    Write-Host "Fetching DAG Mod 1.10.0 from Modrinth..."
    Invoke-WebRequest 'https://cdn.modrinth.com/data/lFbgrVlP/versions/L71Ja93p/dagmod-1.10.0.jar' -OutFile $dagJar
}

$manifest = Get-Content (Join-Path $root 'manifest.json') -Raw | ConvertFrom-Json
$version = $manifest.version
$out = Join-Path $root "build/medieval-fantasy-craft-$version.zip"

New-Item -ItemType Directory -Force (Join-Path $root 'build') | Out-Null
if (Test-Path $out) { Remove-Item $out -Force }

Compress-Archive -Path (Join-Path $root 'manifest.json'), (Join-Path $root 'modlist.html'), (Join-Path $root 'overrides') -DestinationPath $out

Write-Host "Built $out"
