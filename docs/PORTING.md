# Porting lagging mods to Minecraft 26.2 ourselves

The pack targets **Minecraft Java 26.2 (Fabric)**. Most of the roster is already there,
but a few mods we want are behind. This doc tracks which ones we can legally update
ourselves, which we can't, and the workflow for doing a port.

## Port candidates (verified 2026-09-01)

| Mod | Stuck at | License | Can we port & redistribute? |
|---|---|---|---|
| YUNG's Better Dungeons + YUNG's API | 26.1.2 | LGPL-3.0 | ✅ Yes — best first target, the version gap is tiny |
| Ars Nouveau | 1.21.1 | LGPL-3.0 (CF) / GPL-3.0 (Modrinth) — check repo LICENSE | ⚠️ Legally yes, but it is NeoForge-only. Getting it onto **Fabric** 26.2 is a rewrite, not a port. Realistically: wait, or pick a Fabric-native magic mod when one reaches 26.2 |
| When Dungeons Arise | 1.21.1 | All Rights Reserved | ❌ Not without the author's permission (source is public — worth asking) |
| Epic Knights | 1.21.1 | No license file → ARR | ❌ Not without permission. Their CF page only permits packing *official* builds |
| Iron's Spells 'n Spellbooks | 1.21.1 | Custom "ALL RIGHTS RESERVED" | ❌ No |
| Small Ships | 1.21.4 | All Rights Reserved | ❌ No |
| Astrocraft (night skies) | 1.21.4 | MIT per CurseForge | ⚠️ Legal, but no public source repo could be found — contact the author |

Before porting anything: **search Modrinth/CurseForge for an existing maintained fork
first.** Someone has often already done the work.

## Workflow: version-porting a Fabric mod (YUNG's example)

1. **Toolchain**: install a recent JDK (check the mod's `gradle.properties` /
   `build.gradle` for the required Java version; 26.x-era mods use the JDK the
   Fabric toolchain currently targets).
2. **Fork and clone** the repo (e.g. `yungnickyoung/YUNGs-Better-Dungeons`), branch off
   the newest release tag.
3. **Bump versions** in `gradle.properties`:
   - `minecraft_version` → `26.2`
   - mappings (yarn/mojmap), `loader_version`, `fabric_api_version` — current values
     are listed at <https://fabricmc.net/develop/>
   - any library deps (YUNG's API for the dungeons mod — port the API first).
4. **Build and fix**: `./gradlew build`. Between 26.1.2 → 26.2 expect renamed
   mappings and small API shifts; between 1.21.x → 26.x expect larger registry/
   rendering changes (26.2 added the experimental Vulkan renderer — anything touching
   rendering must stay on the OpenGL path, same as Iris/DH do).
5. **Test in dev**: `./gradlew runClient`, generate a world, verify the structures
   actually spawn (`/locate structure`).
6. **License compliance (LGPL)**: keep the LGPL-3.0 license, publish your modified
   source (your GitHub fork counts), and note your changes.
7. **Ship it** — two options:
   - **overrides/mods/**: drop the built jar in the pack's `overrides/mods/` folder.
     Legal for LGPL mods with source published; CurseForge moderation allows
     overrides jars you have rights to.
   - **Own CF project**: upload the fork as its own CurseForge project (clearly marked
     unofficial, linking the original), then reference it in `manifest.json` like any
     other mod. Cleaner for pack updates, and lets others use it.

## When 26.3 lands (due September 2026)

Same drill, one version further: wait ~2–6 weeks for Fabric API / Sodium / Iris / DH
to publish 26.3 builds, bump `manifest.json`, and re-check this table — some of the
stragglers may have caught up on their own.
