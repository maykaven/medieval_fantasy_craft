# Heritage skins

Three original player skins, one per DAG heritage — dwarf, elf, orc. Drawn
procedurally by [make_skins.py](make_skins.py), so they are our own work and safe
to publish, per the licensing ground rules in
[../docs/MYTHFOLK-PLAN.md](../docs/MYTHFOLK-PLAN.md).

| File | Model | Notes |
|---|---|---|
| `dwarf.png` | classic | Mouth inside the beard, gold beard-rings, beard runs to the belt |
| `elf.png` | **slim** | Gold circlet, studded embroidery, bare pointed ear tips |
| `orc.png` | classic | Red warpaint, tusks, bare muscled chest, hide harness |

The elf is drawn on the **slim** (Alex, 3px arm) layout. Registering it as classic
stretches its arms wrong.

## Install into an instance

With Minecraft **closed**:

```
python skins/add_presets.py "<instance folder>"
```

That copies the PNGs into `config/skinshuffle/skins/` and adds a preset for each,
leaving existing presets alone. It must run with the game closed — Skin Shuffle
holds presets in memory and rewrites `presets.json` on exit, so a live edit is
discarded.

The PNGs are also shipped in `overrides/config/skinshuffle/skins/`, so a fresh
pack install already has the files on disk; only the presets need adding.

## Requires

Skin Shuffle, plus YetAnotherConfigLib which it depends on. Neither is bundled in
the pack — see the client-side section of
[../docs/MODLIST.md](../docs/MODLIST.md) for why and where to get them.
3D Skin Layers is optional but worth having, for the reason below.

## How the detail works

Two things carry these beyond flat recolours.

**Features cross body parts.** A beard painted only on the head texture is bounded
by the head cube and can never reach past the chin. The dwarf's beard is painted
onto the *torso* texture as well, so it runs unbroken from his face to his belt.

**Layer 2 is geometry, not paint.** 3D Skin Layers renders the skin's outer layer
with real depth, so the dwarf's beard, the elf's hair mane and the orc's harness
stand off the model instead of lying flat. Two rules follow from that:

- Layer 2 must stay **transparent** wherever it is not authored. Filling it opaque
  buries whatever is underneath — an early version hid the dwarf's whole face
  behind solid beard.
- Anything on layer 1 that must remain visible needs a **gap cut** in layer 2
  above it. That is how the dwarf's mouth reads through his beard.

Every visible face is a hand-authored pixel map — one character per pixel against
a per-race palette — rather than a rectangle fill. Rectangles give bands of
colour; they cannot place a mouth inside a beard or a tendon on a forearm at
64×64. Each cube face is also lit separately (front 1.0, left 0.95, right 0.87,
back 0.79) so the figures read as solid rather than flat.

## Resolution

These are 64×64, which is vanilla's limit. Every pixel is doing work, so more
detail means an HD-skin mod rather than better art — and that would put a third
mixin into skin rendering alongside Skin Shuffle and 3D Skin Layers, so check
compatibility before committing to it.

## Interaction with racescale

[../racescale/](../racescale/) counter-scales the head on dwarves and elves to keep
it natural-sized on a shorter or taller body. That is where 3D Skin Layers' raised
hair layer is most likely to sit slightly proud of the head. Orcs scale uniformly
and will not show it.
