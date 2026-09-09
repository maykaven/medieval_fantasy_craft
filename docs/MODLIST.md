# Mod list — Medieval Fantasy Craft

Target: **Minecraft Java 26.2, Fabric loader 0.19.5.** All versions/IDs verified
against CurseForge on **2026-09-01**. File IDs are the exact 26.2 Fabric files
pinned in [manifest.json](../manifest.json).

## In the pack

### Rendering & performance

| Mod | Version | Project ID | File ID | Notes |
|---|---|---|---|---|
| Fabric API | 0.159.0+26.2 | 306612 | 8784305 | Base library |
| Sodium | 0.9.1 | 394468 | 8396428 | Renderer; required by Iris (still a separate jar) |
| Iris Shaders | 1.11.2+26.2 | 455508 | 8396841 | Shader engine; matched to Sodium 0.9.1 |
| Distant Horizons | 3.2.0-b | 508933 | 8389161 | LOD renderer, one jar for Fabric+NeoForge; the "insane view distance" |
| Lithium | 0.25.3 | 360438 | 8533307 | Server/tick optimization |
| FerriteCore | 9.0.0 | 459857 | 7806040 | Memory usage — matters at big LOD radii |
| Entity Culling | 1.10.5 | 448233 | 8287118 | Skips rendering hidden entities |
| ImmediatelyFast | 1.16.4 | 686911 | 8749433 | Rendering batch optimization |
| ScalableLux | 0.2.1 | 1055925 | 8235664 | Starlight-based light engine — faster light updates during chunk gen (by C2ME's org) |
| Fast Noise | 1.0.40+26.2 | 1460602 | 8639892 | Worldgen noise optimization (~10–18% faster gen), datapack-safe with Terralith/Tectonic. Successor to archived Noisium |
| BadOptimizations | 2.4.1 | 949555 | 8260341 | Client tick: lightmap-update and sky-color caching |
| Particle Core | 0.3.3+26.2 | 985426 | 8390340 | Particle culling and render optimization; Sodium-verified |
| MoreCulling | 1.8.1 | 630104 | 8563691 | Culls blockstates, leaves, item frames, sign text. Needs Cloth Config. If a modded block face ever vanishes, toggle the matching option in its settings |
| FastQuit | 3.1.5 | 708967 | 8537736 | Exit to title immediately; world saves in the background |
| Krypton | 0.3.1 | 428912 | 8433993 | Network stack optimization — marginal in singleplayer, matters when hosting |
| C2ME | 0.4.1-beta.1.0 | 533097 | 8294509 | **Optional (unticked at import)** — multithreaded chunk generation, the biggest worldgen speedup on many-core CPUs (Terralith-benchmarked; pairs with Lithium + ScalableLux per its own docs). Has DH interop history: test your first session; if world load freezes or errors spam, set `gcFreeChunkSerializer=false` and `replaceImpl=false` in `config/c2me.toml`, or remove it |

### Libraries (dependencies)

| Mod | Version | Project ID | File ID | Needed by |
|---|---|---|---|---|
| Cloth Config API | v26.2.155 | 348521 | 8269699 | Better Combat |
| Player Animation Library | 1.2.6+26.2 | 1283899 | 8674798 | Better Combat (successor of playerAnimator) |
| Cristel Lib | 3.1.10 | 856996 | 8451603 | Towns and Towers |
| Lithostitched | v1.8.0+beta3 | 936015 | 8637573 | ChoiceTheorem's Overhauled Village (needs 3.4.4+… project versioning differs; this is the newest 26.2 release-channel file) |
| Balm | 26.2.0.7 | 531761 | 8777987 | Waystones |
| Shogi | 26.2.0.5 | 1475746 | 8645591 | Waystones (26.1+) |

### World generation & structures

| Mod | Version | Project ID | File ID | Notes |
|---|---|---|---|---|
| Terralith | 2.6.4 | 513688 | 8394239 | Stardust Labs biomes/terrain |
| Tectonic | 3.0.26 | 686836 | 8360835 | Dramatic terrain; Terralith-compat ("Terratonic") is built into the mod jar |
| Towns and Towers | 1.13.11 | 626761 | 7886369 | 50+ village/structure variants; universal jar |
| ChoiceTheorem's Overhauled Village | 4.1.0 | 623908 | 8754947 | Medieval-styled village overhaul |

### Gameplay

| Mod | Version | Project ID | File ID | Notes |
|---|---|---|---|---|
| Better Combat | 3.2.2+26.2 | 639842 | 8486571 | Directional melee combat |
| Farmer's Delight Refabricated | 3.6.21 | 993166 | 8787634 | Cooking/farming (the only Farmer's Delight on 26.2; Fabric-only, MIT) |
| Waystones | 26.2.0.11 | 245755 | 8778790 | Fast travel between discovered waystones |

### Fantasy races & creatures

| Mod | Version | Project ID | File ID | Notes |
|---|---|---|---|---|
| DAG Mod | 1.10.0 | Modrinth `lFbgrVlP` | embedded jar | **RPG edition only.** Playable Human/Dwarf/Elf/Orc races × Warrior/Mage/Rogue classes, quests, merchant NPCs, bosses, extra dimensions. CC0 — jar embedded in overrides-rpg/mods (fetched by build.ps1, ~97MB, not on CurseForge). Experimental: small solo project, remove `dagmod-*.jar` from the instance mods folder if it misbehaves |
| Freecam | 1.4.1 | Modrinth `XeEZ3fK2` | embedded jar | **Both editions.** Detached out-of-body camera - toggle it, then "Control Player" to move your body while the camera stays put, and "Toggle Outline Player" to find yourself. MIT, client-side only, fetched by build.ps1. Keybinds under Options -> Controls -> Freecam. Version-bound to `<26.3.0-0`, so it needs a bump with 26.3 |
| Race Scale | 0.1.0 | ours | embedded jar | **RPG edition only.** Shapes the player body to the race registered with DAG's Innkeeper Garrick: dwarf 20% shorter, elf 20% taller (both keeping a natural-sized head), orc 10% bigger all over. Reads DAG's own race attribute modifiers, so registering with Garrick is the only step. Source in `racescale-mod/`, built with `bash racescale-mod/build.sh` (needs JDK 25) |
| Goblin Traders | 1.12.0 | 363703 | 8403603 | Goblin merchant NPCs underground and in the Nether (MrCrayfish official). Requires Framework |
| Framework | 0.13.26 | 549225 | 8403587 | Goblin Traders dependency |
| Illager Invasion | 26.2.0 | 891324 | 8275993 | New illager types, structures and raid pressure — the closest 26.2-Fabric thing to orc war bands. Requires Puzzles Lib + Forge Config API Port |
| Puzzles Lib | 26.2.3 | 495476 | 8581779 | Illager Invasion dependency |
| Forge Config API Port | 26.2.1 | 547434 | 8292030 | Illager Invasion dependency |

**Watch list for the real payoff:** [Middle-earth by Jukoz](https://modrinth.com/mod/middle-earth) — full elves/dwarves/orcs factions with gear and world content, Fabric, currently 1.21.8 beta; check monthly for a 26.x build and add it the moment it lands. Runners-up: Iourus Races (exact races, 26.2 but NeoForge-only), Bokoblins (26.x NeoForge-only), Mobs of Mythology (1.21.1). Alternatives to DAG if it disappoints: Origins: Legacy (CF 1429195, the 26.2 Origins engine — its stock origins aren't fantasy races though) or Fabled Roots (Modrinth, race analogues, GPL3).

### Sky & shaders

| Item | Version | Project ID | File ID | Notes |
|---|---|---|---|---|
| Nuit | 1.0.0-beta.4 | 408209 | 8294703 | Skybox engine (FabricSkyboxes renamed). Nuit Interop NOT needed — our sky pack is Nuit-native. Known: Nether skies don't work yet |
| Continuity | 3.0.1+26.2 | 531351 | 8261100 | OptiFine-format connected textures on Fabric (Sodium/Iris-compatible). Required by Patrix — without it Patrix grass renders an "enable connected textures" placeholder |
| Entity Model Features | 3.3.3 | 844662 | 8792272 | OptiFine-format custom entity models — required for Patrix/Fresh Animations mob models to render correctly. ⚠️ Do NOT install the "EMF Compat" bridge mods (emf_compat_core) — built for 3.3.2's API, crash with 3.3.3 |
| Entity Texture Features | 7.2.1 | 568563 | 8789258 | OptiFine-format entity textures (random/emissive variants), Iris-aware — pairs with EMF |
| Mod Menu | 20.0.1 | 308702 | 8402669 | In-game settings screens for Fabric mods (Continuity, ETF, etc.) |
| Text Placeholder API | 3.1.0-beta.1 | 1037459 | 8271471 | Mod Menu dependency |
| Not Enough Animations | 1.12.4 | 433760 | 8274928 | Player animations: eating, map-holding, climbing, boat-rowing. Works standalone — no EMF bridge needed |
| Fabric Language Kotlin | 1.14.1+kotlin.2.4.20 | 308769 | 8829788 | Particle Core dependency (Kotlin runtime). 1.14+ requires Fabric Loader 0.19.5+ — keep the manifest's loader id in sync when updating this mod |
| Fzzy Config | 0.7.6+26.2 | 1005914 | 8261915 | Particle Core dependency (config library) |
| Bliss Shader | v2.1.2 | 610844 | 7251787 | **Default shader.** Tagged 26.2; ≥2.1.0 = Distant Horizons support |
| Photon Shader | v1.3b | 1312687 | 7927503 | **Optional.** Best realistic sun/moon/sky, DH support — but newest tag is 26.1.2, unconfirmed on 26.2. Marked non-required in the manifest |
| Hyper Realistic Sky | v3.9 | 622551 | 8285672 | Resource pack, Nuit-native format, tagged 26.2. Realistic sun/moon/clouds when shaders are off |
| Epic Adventures | 1.21.11+67 | 406771 | 8533674 | **Optional alternate base pack** — 32x stylized-realistic medieval fantasy. Newest tag is 1.21.11: loads on 26.2 with an "older pack" warning; 26.2's new blocks fall back to vanilla textures until it updates |
| Patrix 32x (basic) | 26.2 | 785390 | 8788976 | **Optional alternative** — realistic, made for shaders (labPBR normals/speculars; enable labPBR options in your shader). Looks wrong without shaders. Only one base pack enabled at a time |
| Fresh Animations | 1.10.5 | 453763 | 7854681 | Lively animal/mob models + animations via EMF (by FreshLX, who also made Patrix's mob animations). **Load ABOVE the base pack** — and above Patrix in particular, where it overrides Patrix's WIP 26.2 mob models with working ones |
| FA: Quivers | 2.2 | 1346077 | 7674520 | Official FA addon — visible quivers on skeletons. Load above base FA |
| FA: Spiders | 2.2 | 1346116 | 7999323 | Official FA addon — reworked spiders. Load above base FA |
| FA: Details | 2.3 | 1346132 | 7999513 | Official FA addon — extra creature detail (26.1+ only; includes former Slamacow content). Load above base FA |
| FA: Emissive | 1.6 | 1346083 | 7999667 | Official FA addon — glowing eyes/parts via ETF. Load above base FA |
| Alacrity | 26.2+38 | 520028 | 8612633 | **Default block/item textures** — 32x rustic-realistic, 100% complete incl. mobs, no shader-PBR (nothing to enable in the shader). Pre-enabled in overrides/options.txt; never two base packs at once |

## Client-side extras (install yourself — deliberately not bundled)

Useful client mods that are **not** in either manifest. All three are restrictively
licensed, and the ground rules in [MYTHFOLK-PLAN.md](MYTHFOLK-PLAN.md) rule out
bundling All-Rights-Reserved work. Installing them personally is fine; shipping
their jars in `overrides/` is not. The clean route for publishing would be
CurseForge manifest entries — a reference rather than redistribution — which needs
their CurseForge project and file IDs.

| Mod | Version | Source | License | Why |
|---|---|---|---|---|
| Skin Shuffle | 2.12.0+26.2 | Modrinth `3s19I5jr` | All Rights Reserved | In-game skin carousel. Needed to use the [heritage skins](../skins/). 26.2 build is beta channel |
| YetAnotherConfigLib | 3.9.6+26.2 | Modrinth `1eAoo2KR` | LGPL-3.0 | Hard dependency of Skin Shuffle — Fabric will not start without it |
| 3D Skin Layers | 1.11.2 | Modrinth `zV5r3pPn` | tr7zw Protective | Renders the skin's outer layer with real depth. The heritage skins put beards, hair and harnesses on layer 2 specifically for this |

Freecam **is** bundled (MIT), fetched from Modrinth by `build.ps1` into
`overrides/mods/` for both editions — an out-of-body camera is how you inspect your
own character.

## Not in the pack yet (watching / porting)

| Mod | Stuck at | License | Plan |
|---|---|---|---|
| YUNG's Better Dungeons + YUNG's API | 26.1.2 | LGPL-3.0 | Port ourselves — see [PORTING.md](PORTING.md) — or wait a few weeks; family updates actively |
| When Dungeons Arise | 1.21.1 | ARR | Wait for official update (Fabric edition: project 511812) |
| Epic Knights | 1.21.1 | ARR (no license file) | Wait for official update; add the moment a 26.x build lands (project 509041) |
| Immersive Structures | 1.21.11 | Custom | Wait (same author as CTOV, likely to follow it) |
| Ars Nouveau | 1.21.1 | LGPL/GPL | NeoForge-only — not portable to Fabric cheaply; magic slot stays open |
| Iron's Spells 'n Spellbooks | 1.21.1 | ARR | Wait |
| Small Ships | 1.21.4 | ARR | Wait (stale ~16 months — may not come) |
| Astrocraft | 1.21.4 | MIT (no public source found) | Optional nicety; contact author |
| Terrarium (real Earth terrain) | 1.21.8 | CC-BY-NC-SA | The only modern "actual Earth" worldgen (Terra 1-to-1 successor). NC license bars CurseForge pack distribution; noted for private use only |

---

## v0.6.0 (World) / v1.2.0 (RPG) — full live-config sync (2026-09-09)

Both manifests were regenerated from the live instance's `minecraftinstance.json`
(authoritative CurseForge project/file IDs), so the install pack now reproduces the
actual played setup: **66 CurseForge-hosted files**, all pinned to the versions in
use. Notable additions since the last itemised tables above:

- **Mods added:** 3D Skin Layers (521480), YetAnotherConfigLib (667299), and
  Freecam moved from a Modrinth-fetch to a CurseForge reference (557076).
- **Version bumps:** Fabric API 0.160.0, Balm 26.2.0.8, Waystones 26.2.0.12,
  Entity Model Features 3.3.5, Lithostitched 1.8.0+beta6, Hyper Realistic Sky v3.10.
- **Resource packs added (all CurseForge-hosted, referenced in the manifest):**
  Round Trees (296616), Realistic Chests (1016013), Freshly Modded / F.M.R.P
  (961754), LowOnFire (580683), Extended Illumina (380413), Actually 3D Blocks &
  Items (1509983), Glow Lichen 3D (1409336), and the Fresh Animations addons
  All-Extensions (813608), Creepers (1346049), Player (1281029).
- **c2me** is marked `required: false` (you have it disabled in the instance).
- **Enabled load order** is captured verbatim in `overrides/options.txt`
  (Patrix + Epic Adventures base → FA + all FA addons → Terrain Blend → Actually 3D
  → Glow Lichen 3D → Hyper Realistic Sky on top).

### ⚠️ One manual add: Skin Shuffle

**Skin Shuffle has no Minecraft 26.2 build on CurseForge** (2.12.0+26.2 is
Modrinth-only) and it's All-Rights-Reserved, so it can't be referenced in a CF
manifest or legally bundled. The [heritage skins](../skins/) need it. After
importing the pack, add it yourself from <https://modrinth.com/mod/skinshuffle>
(its deps 3D Skin Layers and YACL are already in the pack). Everything else installs
automatically.
