# Race body scaling

Scales the **player avatar** to match the race picked from DAG Mod's Innkeeper
Garrick in the Fantasy RPG edition.

| Race | Scale | Result | Standing height |
|---|---|---|---|
| Human | `1.0` | unchanged | 1.80 blocks |
| Dwarf | `0.8` | 20% shorter | 1.44 blocks |
| Elf | `1.2` | 20% taller | 2.16 blocks |
| Orc | `1.1` | 10% bigger overall | 1.98 blocks |

## Why equipment always fits

This uses the vanilla **`minecraft:scale`** attribute rather than a rendering
trick. Minecraft applies that attribute to the whole entity: the body model, every
armour layer, held items, the hitbox and the eye height all scale by the same
factor together. So armour, clothing and tools fit any race automatically, with no
per-item work and no compatibility patching — a dwarf's chestplate is simply drawn
at 0.8 along with the dwarf.

That is the entire reason for choosing the attribute over a `PoseStack` scale in a
renderer: an attribute is authoritative for both rendering and physics, so nothing
can drift out of sync.

## Orcs: 10% bigger overall, not 20% wider

Orcs scale uniformly to `1.1` — 10% larger in every direction. That reads as
imposing, keeps equipment fitting for free like every other race, and at 1.98
blocks tall still clears standard 2-block doorways without sneaking.

True *width* is a different problem. "20% wider" is **non-uniform** scaling — X and
Z only, leaving Y alone. The vanilla `scale` attribute is uniform by definition, and
there is no vanilla attribute, command or data-driven way to stretch one axis of an
entity. Resource packs cannot help either: the player model is hardcoded,
OptiFine/EMF custom entity models do not cover the player, and armour is a separate
model that would not follow anyway.

Getting genuine width needs a small Fabric mod:

1. **Render** — mixin into `LivingEntityRenderer#scale` (the hook that runs *before*
   the model and all of its armour layers) and apply
   `poseStack.scale(1.2F, 1.0F, 1.2F)` for orcs. Because armour renders as layers
   inside that same pose, the armour widens with the body and keeps fitting. This is
   the same reasoning as above, applied at the one point where all layers share a
   transform.
2. **Physics** — mixin `Player#getDimensions` to return
   `EntityDimensions.scalable(width * 1.2F, height)` so the hitbox matches.
3. **Race source** — read `dagmod_race` (see below) rather than a scoreboard.

That work belongs with Mythfolk Phase 2, which is already the repo's designated
place for Java (see [../docs/MYTHFOLK-PLAN.md](../docs/MYTHFOLK-PLAN.md)). It needs
a JDK + Gradle/Loom toolchain, neither of which is installed on this machine.

## Why you pick the race manually

DAG Mod persists the choice to **world files** at
`saves/<world>/data/dagmod/players/<uuid>.dat` (gzipped NBT: `dagmod_race`,
`dagmod_class`), not to player NBT or a scoreboard. Its race bonuses are applied as
**transient** attribute modifiers, so they are not saved into the player either.
Nothing a datapack can read, in other words — reading it needs Java. One extra
command per character is the honest trade.

## Use

Works with **cheats off**: `/trigger` runs at permission level 0.

```
/trigger racescale_pick set 1    # human
/trigger racescale_pick set 2    # dwarf
/trigger racescale_pick set 3    # elf
/trigger racescale_pick set 4    # orc
```

With cheats on you can instead run `/function racescale:race/dwarf`, or
`/function racescale:reset` to go back to normal.

The scale re-applies automatically after death, because respawning rebuilds the
player entity and resets its attributes.

## Install

A datapack is per-world and cannot be shipped through `overrides/`, so copy this
folder into a world:

```
saves/<world>/datapacks/racescale/
```

New datapacks are picked up when the world loads. `/reload` also works but needs
cheats, so with cheats off just exit to the title screen and re-enter the world.

## Tuning

Edit the four values in `data/racescale/function/apply.mcfunction`. Note that an elf
at `1.2` stands 2.16 blocks tall and must sneak through standard 2-block doorways;
`1.1` (1.98 blocks) still reads as noticeably tall while fitting everywhere.

Data pack format is `107`, taken from Terralith 26.2 — the authoritative 26.2 value.
