# Builds the CurseForge-importable modpack zip into build/
$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot

$manifest = Get-Content (Join-Path $root 'manifest.json') -Raw | ConvertFrom-Json
$version = $manifest.version
$out = Join-Path $root "build/medieval-fantasy-craft-$version.zip"

New-Item -ItemType Directory -Force (Join-Path $root 'build') | Out-Null
if (Test-Path $out) { Remove-Item $out -Force }

Compress-Archive -Path (Join-Path $root 'manifest.json'), (Join-Path $root 'modlist.html'), (Join-Path $root 'overrides') -DestinationPath $out

Write-Host "Built $out"
