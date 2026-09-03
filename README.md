# Medieval Fantasy Craft

A medieval-fantasy CurseForge modpack for **Minecraft Java 26.2 "Chaos Cubed"** on
**Fabric** — dramatic realistic landscapes, an absurd view distance, cinematic
shaders, a realistic sun/moon skybox, and a world full of villages, castles,
dungeons and knights.

## The pillars

| Goal | How |
|---|---|
| Realistic landscape | **Terralith + Tectonic** worldgen (Tectonic's Terralith-compat "Terratonic" mode is built into the mod jar — just install both) |
| Insane view distance | **Distant Horizons 3.2** LOD renderer — far terrain out to hundreds of chunks (configurable up to 4096) |
| Great shaders | **Iris + Sodium**, with **Bliss v2.1.2** as the default shader (verified on 26.2, shades Distant Horizons' far terrain). **Photon** included as the optional cinematic pick — best-in-class realistic sun/moon/sky, but its newest build is tagged 26.1.2, so treat it as "try and see" until it updates |
| Real skybox sun & moon | **Nuit** (successor of FabricSkyboxes) + the **Hyper Realistic Sky** resource pack (v3.9, Nuit-native format) |
| Medieval fantasy world | **Towns & Towers**, **ChoiceTheorem's Overhauled Villages**, **Better Combat**, **Farmer's Delight Refabricated**, **Waystones** |
| Medieval look | **Epic Adventures** 32x textures (stylized-realistic medieval fantasy) as the default, **Patrix 32x** as the optional shader-maxed realistic alternative |
| Fantasy races | **DAG Mod** — playable Elf/Dwarf/Orc/Human with classes and quests (embedded, experimental); **Goblin Traders** and **Illager Invasion** populate the world. The full elves/dwarves/orcs faction experience arrives when the Middle-earth mod reaches 26.x (see docs/MODLIST.md watch list) |

Full mod list with versions, IDs and licenses: [docs/MODLIST.md](docs/MODLIST.md).
Mods still stuck on older Minecraft (and how we port them ourselves): [docs/PORTING.md](docs/PORTING.md).

## Building the pack zip

```powershell
./build.ps1
```

This produces `build/medieval-fantasy-craft-<version>.zip` containing
`manifest.json`, `modlist.html` and `overrides/` — the exact format the CurseForge
app imports and the CurseForge site accepts as a modpack submission.

## Installing locally (CurseForge app)

1. CurseForge app → Minecraft → **Create Custom Profile** → **Import** → pick the
   built zip. The app downloads every mod from the manifest automatically.
2. Open the profile's settings and allocate **8–12 GB of RAM** (Distant Horizons at
   large radii is memory-hungry).
3. Launch.

## First-launch checklist (in-game)

1. **Stay on OpenGL.** 26.2 ships an experimental Vulkan renderer — do **not**
   enable it. Iris shaders silently turn off under Vulkan, and Distant Horizons'
   shader integration is OpenGL-only.
2. **Shaders**: Options → Video Settings → Shader Packs → select **Bliss**. Feeling
   lucky? Try **Photon** for the most realistic sun/moon/sky — if it misbehaves on
   26.2, switch back to Bliss until Photon ships a 26.2 build.
3. **View distance — pre-configured**: Distant Horizons ships hard-wired to a
   **512-chunk LOD radius** (~8 km horizon) with generation capped to match and
   CPU threading tamed (8 threads at half run-time) so the internal server never
   starves — uncapped generation causes tick lag that "rewinds" fast block
   breaking. Vanilla render distance stays at 12; DH draws everything beyond it.
   The first hour in a new area generates the horizon in the background, then
   it's cached. Don't raise maxGenerationRequestDistance above the render
   radius.
   - If the far sky/terrain ever looks broken with shaders: DH → Advanced →
     Advanced Graphics Settings → **Transparency = Complete**, **Render Quality =
     Medium**, then restart.
4. **Resource packs — pre-configured**: the pack ships with the proven setup
   already enabled, top → bottom: **Hyper Realistic Sky → FA addons (Spiders,
   Quivers, Emissive, Details) → Fresh Animations → Patrix**. Verify it looks
   like that and you're done. For Patrix, turn on the labPBR emissive/subsurface
   options in Bliss's shader settings — it's built for shaders and looks wrong
   without them. (Continuity, EMF and ETF in the pack supply the connected
   textures and entity models/textures everything here depends on.)
   Alternate base looks — swap into Patrix's bottom slot, **never two base packs
   at once** (stacked base packs mix entity textures and mobs render broken):
   **Alacrity** (rustic-realistic, complete) or **Epic Adventures** (painterly
   medieval; tagged 1.21.11 — confirm the "older version" prompt, fine on 26.2).
   Whatever the base, **Fresh Animations stays above it** so its animal models
   win.
   *Expectation check:* while a shader pack is active, the shader draws its own sky
   — and Photon's realistic sun, moon and Milky Way are the star of the show. The
   Nuit + Hyper Realistic Sky skybox is what makes the sky gorgeous when you play
   *without* shaders (or with the vanilla-ish shader options).
5. **World creation**: default world type — Terralith/Tectonic hook into normal
   generation. Fly somewhere high and look at the horizon.

## Known caveats (as of 2026-09-01)

- **DH 3.2.0-b + Iris**: far-terrain LODs are fully *shaded* but Iris doesn't yet
  draw DH's new LOD *textures* — a known cosmetic issue awaiting an Iris-side fix.
- **Photon**: no 26.2-tagged release yet (newest is 26.1.2) — included as optional,
  unverified on 26.2. Bliss is the verified default.
- **Nuit**: Nether skies don't work yet with the Hyper Realistic Sky pack.
- **Do not install the "EMF Compat" bridge mods** (emf_compat_core /
  emf_compat_not_enough_animations): they target EMF 3.3.2's API and crash the
  game with the EMF 3.3.3 in this pack. Not Enough Animations works fine
  without them.
- **C2ME is optional** (multithreaded chunk generation — big worldgen speedup on
  many-core CPUs, but it has interop history with Distant Horizons). If you
  enable it, test one session: on world-load freezes or log error spam, set
  `gcFreeChunkSerializer=false` and `replaceImpl=false` in `config/c2me.toml`,
  or remove the mod. Skip Nvidium entirely — it turns itself off while Iris
  shaders are active, so it does nothing in this pack.
- **Patrix mobs on 26.2 are work-in-progress upstream**: with EMF custom models
  on, Patrix's own animal models render distorted (misplaced legs/heads). Fix:
  keep **Fresh Animations enabled ABOVE Patrix** in the resource pack list — its
  working animal models (by the same animator who made Patrix's) override the
  broken ones. Keep EMF custom models ON for this to work.
- **Magic mods**: nothing in the Ars Nouveau / Iron's Spells class has reached 26.2
  yet (they're on 1.21.1). See [docs/PORTING.md](docs/PORTING.md) for the plan.
- **26.3** lands this month; the pack bumps once Fabric API / Sodium / Iris / DH
  publish 26.3 builds.

## Publishing on CurseForge

1. <https://www.curseforge.com> → sign in → **Start a Project** → **Modpack**.
2. Fill out name, summary, description, license, and a logo image.
3. Upload the built zip from `build/` as the first file (mark it Beta while testing).
4. A CurseForge moderator reviews it before it goes public (usually a few days).
   All mods referenced in the manifest are CurseForge-hosted, which is what
   moderation checks for.
