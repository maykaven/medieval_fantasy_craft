# Builds the CurseForge-importable modpack zips into build/
#   ./build.ps1              -> both editions
#   ./build.ps1 -Variant world  -> Medieval Fantasy Craft (world systems only)
#   ./build.ps1 -Variant rpg    -> Medieval Fantasy Craft RPG (+ races/classes)
param([ValidateSet('world','rpg','all')][string]$Variant = 'all')
$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot

function Build-Pack($manifestFile, $modlistFile, $extraOverrides, $slug) {
    $manifest = Get-Content (Join-Path $root $manifestFile) -Raw | ConvertFrom-Json
    $out = Join-Path $root "build/$slug-$($manifest.version).zip"
    $stage = Join-Path $root "build/stage-$slug"
    if (Test-Path $stage) { Remove-Item $stage -Recurse -Force }
    New-Item -ItemType Directory -Force $stage | Out-Null
    Copy-Item (Join-Path $root $manifestFile) (Join-Path $stage 'manifest.json')
    Copy-Item (Join-Path $root $modlistFile) (Join-Path $stage 'modlist.html')
    Copy-Item (Join-Path $root 'overrides') (Join-Path $stage 'overrides') -Recurse
    if ($extraOverrides) {
        Copy-Item (Join-Path $root "$extraOverrides/*") (Join-Path $stage 'overrides') -Recurse -Force
    }
    if (Test-Path $out) { Remove-Item $out -Force }
    Compress-Archive -Path (Join-Path $stage 'manifest.json'), (Join-Path $stage 'modlist.html'), (Join-Path $stage 'overrides') -DestinationPath $out
    Remove-Item $stage -Recurse -Force
    Write-Host "Built $out"
}

# Freecam (MIT, client-side) - Modrinth-only, so fetched rather than listed in the
# manifest. Ships in both editions: an out-of-body camera is generally useful, and
# it is how you inspect your own character.
$freecamJar = Join-Path $root 'overrides/mods/freecam-fabric-1.4.1+mc26.2.jar'
if (-not (Test-Path $freecamJar)) {
    New-Item -ItemType Directory -Force (Join-Path $root 'overrides/mods') | Out-Null
    Write-Host "Fetching Freecam 1.4.1 from Modrinth..."
    Invoke-WebRequest 'https://cdn.modrinth.com/data/XeEZ3fK2/versions/r125dZ2j/freecam-fabric-1.4.1%2Bmc26.2.jar' -OutFile $freecamJar
}

if ($Variant -in @('rpg','all')) {
    # Modrinth-only embedded jar (CC0); fetched, not committed
    $dagJar = Join-Path $root 'overrides-rpg/mods/dagmod-1.10.0.jar'
    if (-not (Test-Path $dagJar)) {
        New-Item -ItemType Directory -Force (Join-Path $root 'overrides-rpg/mods') | Out-Null
        Write-Host "Fetching DAG Mod 1.10.0 from Modrinth..."
        Invoke-WebRequest 'https://cdn.modrinth.com/data/lFbgrVlP/versions/L71Ja93p/dagmod-1.10.0.jar' -OutFile $dagJar
    }

    # Our own race-scaling mod is committed (7KB) but built from source, so fail
    # loudly rather than shipping an RPG zip without it.
    $raceJar = Join-Path $root 'overrides-rpg/mods/racescale-0.1.0.jar'
    if (-not (Test-Path $raceJar)) {
        throw "Missing $raceJar - build it with: bash racescale-mod/build.sh"
    }
}
if ($Variant -in @('world','all')) { Build-Pack 'manifest.json' 'modlist.html' $null 'medieval-fantasy-craft' }
if ($Variant -in @('rpg','all'))   { Build-Pack 'manifest.rpg.json' 'modlist.rpg.html' 'overrides-rpg' 'medieval-fantasy-craft-rpg' }
