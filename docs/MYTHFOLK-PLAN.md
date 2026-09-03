# Mythfolk — our own fantasy-races project

**Goal:** elves, dwarves, and orcs living in the world — our own work, publishable
on CurseForge under our name, usable by both pack editions (World and RPG).

## Ground rules (legal)

- **Never copy assets out of other mods.** Nearly everything we surveyed (Epic
  Knights, Born in Chaos, When Dungeons Arise, Iron's Spells…) is All Rights
  Reserved, art included. Extract-and-bundle = copyright infringement on publish.
- **Allowed sources:** DAG Mod assets (**CC0** — free for any use), Fabled Roots
  (**GPL3** — attribution + share-alike), and **original art we make**
  (mob textures are 64×64 pixel art).
- Our own licensing when we publish: **MIT for code/data, CC-BY-4.0 for art**
  (decide finally before first upload).

## Architecture — two phases

### Phase 1: datapack + resource pack (NO Java)

Uses tech already in the pack: **ETF** (rule-based entity retexturing) and
vanilla **jigsaw structures** via datapack. Fully ours, fully publishable.

| Race | Base entity | Where | Structure |
|---|---|---|---|
| Wood elves | Villager (retextured via ETF biome rules) | Forest/birch/dark-forest biomes (incl. Terralith forests) | Elven treetop village (jigsaw) |
| Dwarves | Villager (retextured) | Mountain/peak biomes | Carved mountain halls (jigsaw, partially underground) |
| Orcs | Pillager/vindicator (retextured) | Badlands/savanna/peaks | Orc war camp (replaces/augments pillager outpost variants) |

**How ETF biome retexturing works:** resource pack file
`assets/minecraft/optifine/random/entity/villager.properties` with rules like
`textures.2=2` + `biomes.2=minecraft:forest minecraft:birch_forest` pointing at
our `villager2.png` (elf skin). Same pattern for pillager → orc. ETF is already
in both pack editions, so this Just Works.

**How jigsaw structures work:** datapack with
`data/mythfolk/worldgen/structure/…`, `structure_set/…`, `template_pool/…` and
`.nbt` templates exported in-game with Structure Blocks. Model the folder layout
on CTOV/Towns & Towers (both are datapack-driven jigsaws on top of vanilla).

### Phase 2: Fabric Java mod (real entities)

Custom `ElfEntity`/`DwarfEntity`/`OrcEntity` with own AI (trades, patrols,
faction hostility), spawn logic, sounds. Art base: DAG's CC0 assets + our
Phase-1 skins. Template: [Fabric example mod](https://fabricmc.net/develop/)
(loom + yarn, same toolchain as docs/PORTING.md). Phase 2 starts only after
Phase 1 ships and tells us what the world actually needs.

## Elven building standards

Fixed decisions every elven structure follows, so buildings stay consistent as the
template pool grows.

### Doorways: 2.5 blocks of clearance

An elf player stands **2.16 blocks** tall (the `racescale` datapack scales elves to
1.2 - see [../racescale/README.md](../racescale/README.md)). A vanilla door gives
only 2 blocks, so elves would have to sneak through their own houses. The elven
doorway is therefore 2.5 blocks of clear opening:

| | left jamb | opening | right jamb |
|---|---|---|---|
| y+2 | birch log | **birch slab, `type=top`** | birch log |
| y+1 | birch log | door, upper half | birch log |
| y | birch log | door, lower half | birch log |

A top slab sits in the upper half of its block, leaving the lower half open. Two
full blocks plus that half gives 2.5. This is exactly the "half block above the
door" pattern - the slab both closes the wall and forms an open transom.

Place one in a test world with `/trigger mythfolk_build set 1` (works without
cheats); it runs `mythfolk:build/elf_door` at your feet, facing north.

Orcs (scale 1.1 = 1.98 blocks) and dwarves (0.8 = 1.44) clear this too, so the
pattern is safe to reuse outside elven builds.

### Not yet possible: a single 2.5-block-tall door block

A door *block* that is itself 2.5 blocks tall needs a custom block with its own
shape and blockstate, which means Java and therefore Phase 2. Vanilla doors are
exactly two blocks and no datapack can change that. The pattern above reaches the
same clearance with vanilla blocks today.

Making the door *look* elven is a Phase 1 job instead: retexture a door variant in
`mythfolk/resourcepack`. Unlike the ETF entity rules, a block retexture applies to
every door of that type in the world, so pick a wood the pack does not otherwise
lean on.

## Milestones

- [x] **M0 — scaffolding**: `mythfolk/datapack` + `mythfolk/resourcepack` with
  correct `pack.mcmeta` files. Formats for 26.2, read off packs that ship for it:
  **data = 107** (Terralith 26.2), **resource = 88** (Patrix 26.2). World
  DataVersion is 4903.
- [ ] **M1 — first elf skin**: one 64×64 villager retexture (`villager2.png`),
  ETF rule limiting it to forest biomes, verified in-game (`/summon villager`
  in a forest vs plains)
- [ ] **M2 — first structure**: build one elven house in a test world, export
  with Structure Block, wire template_pool → structure → structure_set,
  verify with `/place structure mythfolk:elven_village` and natural generation
- [ ] **M3 — elves complete**: 3–4 skin variants, treetop village pool
  (5+ buildings, paths, jigsaw connections), spawns in Terralith forests
- [ ] **M4 — dwarves** (mountain halls) and **orcs** (war camps) by the same
  pipeline
- [ ] **M5 — ship it**: fold into both editions' overrides, playtest, then
  publish as own CurseForge project ("Mythfolk"), license files included
- [ ] **Phase 2 kickoff** (separate plan when we get there)

## Workflow on any PC

1. `git clone https://github.com/maykaven/medieval_fantasy_craft.git`
2. Work lives in `mythfolk/` — plain text/JSON/PNG, no build tools needed for
   Phase 1. Pixel-art editor: Aseprite/Piskel/GIMP; skins are standard
   villager/pillager texture layouts (pull vanilla ones from the version jar as
   tracing references — reference only, redraw, don't ship them).
3. Test loop: copy `mythfolk/datapack` into a test world's `datapacks/` folder,
   `mythfolk/resourcepack` into `resourcepacks/`, `/reload` for datapack edits.
4. Commit + push; continue on the other machine.

## Watch list (don't duplicate what's coming)

**Middle-earth by Jukoz** (Fabric, at 1.21.8) will eventually deliver full
elf/dwarf/orc factions. Mythfolk Phase 1 is worth doing regardless — it's
lightweight, ours, and tuned to OUR worldgen — but check monthly before
committing to Phase 2's entity work.
