# Terrain Blend (custom)

Grass and dirt creep a soft fringe onto neighbouring blocks (stone, wood, brick,
~300 solid blocks) instead of ending in a hard seam. A GPL-3.0 derivative of
**Grass Overlay** by Hiveko, extended by us. Requires **Continuity** (already in
both pack editions); it drives the OptiFine-format overlay CTM.

## What's here

```
terrain-blend/
  pack.mcmeta                     pack format 34..107 (covers 26.2)
  assets/minecraft/optifine/ctm/_overlays/
    03_grass_block/               grass fringe (biome-tinted green)
    04_dirt_block/                dirt fringe (brown baked in, no tint)
    02_moss_block/ 01_pale_moss_block/   from the original pack, untouched
  LICENSE      GPL-3.0 (retained from the original)
  CHANGES.txt  what we changed vs the original
```

## How a `<block>.properties` works

Each overlay folder has a `.properties` that wires it up:

| key | meaning |
|---|---|
| `method=overlay` | draw a fringe layer on top of a neighbour, chosen by connection pattern |
| `tiles=0-16` | 17 fringe shapes, one per way the source block can touch this face |
| `connectBlocks=grass_block` | the block we blend FROM |
| `matchBlocks=<~300>` | the blocks that RECEIVE the fringe |
| `faces=sides top` | which faces of the receiving block get it (sides = walls/cliffs, the main effect) |
| `tintIndex=0` `tintBlock=grass_block` | multiply the grey tiles by biome grass colour (grass only; dirt bakes brown in and omits this) |
| `layer=cutout` | hard-edged alpha |

The numbered tiles (`0.png`..`16.png`) are mostly-transparent PNGs; only the
fringe pixels are opaque, so the neighbour's own texture shows through. Continuity
picks the tile matching the local grass/dirt connection pattern.

## Known limitation

Overlay CTM blends onto **vertical faces and tops beneath the source** — great on
hills, cliffs, dug areas and building bases. It **cannot** softly dissolve two flat
blocks sitting side-by-side at the same height (a flat grass field meeting a flat
stone path stays a hard seam) — there's no vertical face there for a fringe to live
on. That's inherent to the technique, not a bug.

## Editing / testing

Plain PNG + text, no build tools. Edit here, then:
- `./build.ps1` zips this folder into each edition's `overrides/resourcepacks/`
  as `Terrain Blend (custom).zip` (the zip is generated, not committed).
- To test live: zip the folder's *contents* (not the folder itself) and drop it in
  an instance's `resourcepacks/`, or point at this folder as an unzipped pack.
- The grass fringe is biome-tinted; under some Continuity+shader combos tinted
  overlays can render grey (Continuity issue #789). If that happens, bake the green
  into `03_grass_block/*.png` the same way `04_dirt_block` bakes brown, and drop the
  `tintIndex`/`tintBlock` lines.

## Ideas to work on

- Add more blocks to `matchBlocks` (any solid full block is fair game).
- Author a moss/podzol/snow "creep" the same way (clone a folder, recolour tiles,
  set `connectBlocks`).
- Retexture the fringe tiles for a chunkier or subtler look.
