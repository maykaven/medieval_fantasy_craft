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
3. **View distance**: Options → Distant Horizons → set LOD render distance to
   **256** to start (push toward 512+ only if RAM/GPU allow; vanilla render
   distance stays at ~12, DH draws everything beyond it). First world load spends a
   few minutes generating LODs — the horizon fills in as you play.
   - If the far sky/terrain ever looks broken with shaders: DH → Advanced →
     Advanced Graphics Settings → **Transparency = Complete**, **Render Quality =
     Medium**, then restart.
4. **Resource packs**: enable **Epic Adventures** (medieval textures — it's tagged
   1.21.11, so confirm the "made for an older version" prompt; fine on 26.2) and
   **Hyper Realistic Sky** on top of it. Prefer maximum realism over medieval
   flavor? Swap Epic Adventures for **Patrix** instead (never both), and turn on
   the labPBR emissive/subsurface options in Bliss's shader settings — Patrix is
   built for shaders and looks wrong without them.
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
