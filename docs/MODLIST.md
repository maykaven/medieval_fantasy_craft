# Mod list — Medieval Fantasy Craft

Target: **Minecraft Java 26.2, Fabric loader 0.19.3.** All versions/IDs verified
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

### Sky & shaders

| Item | Version | Project ID | File ID | Notes |
|---|---|---|---|---|
| Nuit | 1.0.0-beta.4 | 408209 | 8294703 | Skybox engine (FabricSkyboxes renamed). Nuit Interop NOT needed — our sky pack is Nuit-native. Known: Nether skies don't work yet |
| Bliss Shader | v2.1.2 | 610844 | 7251787 | **Default shader.** Tagged 26.2; ≥2.1.0 = Distant Horizons support |
| Photon Shader | v1.3b | 1312687 | 7927503 | **Optional.** Best realistic sun/moon/sky, DH support — but newest tag is 26.1.2, unconfirmed on 26.2. Marked non-required in the manifest |
| Hyper Realistic Sky | v3.9 | 622551 | 8285672 | Resource pack, Nuit-native format, tagged 26.2. Realistic sun/moon/clouds when shaders are off |
| Epic Adventures | 1.21.11+67 | 406771 | 8533674 | **Default block/item textures** — 32x stylized-realistic medieval fantasy. Newest tag is 1.21.11: loads on 26.2 with an "older pack" warning; 26.2's new blocks fall back to vanilla textures until it updates |
| Patrix 32x (basic) | 26.2 | 785390 | 8788976 | **Optional alternative** — realistic, made for shaders (labPBR normals/speculars; enable labPBR options in Bliss). Looks wrong without shaders. Pick Epic Adventures OR Patrix, not both |

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
