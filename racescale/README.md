# Race body scaling

Shapes the **player avatar** to the race picked from DAG Mod's Innkeeper Garrick in
the Fantasy RPG edition.

Two parts, with a clean split of responsibility:

| Part | Job |
|---|---|
| `racescale/` (this datapack) | owns *which race you are* — the `racescale_race` scoreboard |
| [`../racescale-mod/`](../racescale-mod/) (Fabric mod) | owns *how you are drawn and how you collide* |

| Race | width (X/Z) | height (Y) | Head | Result | Standing height |
|---|---|---|---|---|---|
| Human | 1.0 | 1.0 | natural | unchanged | 1.80 blocks |
| Dwarf | 1.0 | **0.8** | **natural** | 20% shorter, same breadth — stocky | 1.44 blocks |
| Elf | 1.0 | **1.2** | **natural** | 20% taller, same breadth — elongated | 2.16 blocks |
| Orc | **1.1** | **1.1** | scales with body | 10% bigger all over | 1.98 blocks |

## Why equipment always fits

The mod applies its scale in `AvatarRenderer#scale`, the hook that runs *before* the
player model and before every one of its render layers. Armour is drawn as layers
inside that same pose, so it stretches with the body and keeps fitting — no
per-item work and no compatibility patching.

Hitboxes are kept honest separately, by mixing into `Entity#getDimensions` and
returning `dimensions.scale(width, height)`. Minecraft ships that two-argument
`EntityDimensions.scale` already, so physics gets exactly the same per-axis
treatment as rendering and the two cannot drift apart.

## Natural heads for dwarves and elves

The body scale is applied to the whole pose, which would carry the head with it, so
for dwarves and elves the head is counter-scaled by the inverse — net effect, a
normal-sized head on a shorter or taller body. That is what makes a dwarf read as
stocky and an elf as elongated, rather than as a shrunken or enlarged human. Orcs
are 10% bigger all over, head included, so they get no compensation.

The counter-scale is applied in `HumanoidModel#setupAnim` rather than in
`PlayerModel`, and that choice matters: **armour models extend the same
`HumanoidModel`** and are handed the same render state, so a helmet is
counter-scaled exactly like the head it sits on. Hooking `PlayerModel` instead
would leave a dwarf wearing a shrunken helmet on a full-size head.

The head scales are written on every call rather than only when a race needs them,
because model instances are shared between entities — a value left behind would
leak onto the next humanoid rendered with that model.

## Why single-axis needs the mod at all

The vanilla `minecraft:scale` attribute is **uniform** by definition — it scales
width, depth and height by one factor. A datapack can therefore make a race
uniformly bigger or smaller, but it can never make an elf taller *without* also
making it wider. There is no vanilla attribute, command or data-driven route to
single-axis scaling, and resource packs cannot help: the player model is hardcoded,
OptiFine/EMF custom entity models do not cover the player, and armour is a separate
model that would not follow.

Hence the split. The datapack keeps the vanilla attribute **neutral at 1.0** — see
the comment in `data/racescale/function/apply.mcfunction` — because applying both
would compound and a dwarf would come out 0.8 × 0.8. Without the mod installed you
still get race declaration, just no change in shape.

## How your race is detected

Registering a heritage with DAG's Innkeeper Garrick is the only step. DAG applies
race attribute modifiers (`dagmod:dwarf_speed`, `dagmod:elf_speed`,
`dagmod:orc_attack` and friends), vanilla syncs attribute modifiers to clients
automatically, and the mod reads them on both sides. No packets, no datapack, no
second command.

That deliberately reads DAG's *observable game state* rather than its storage: the
race itself is persisted to world files under `data/dagmod/players/` and DAG exposes
no API, so the alternatives were parsing its save format or mixing into its private
classes. If DAG ever renames those modifiers, this degrades to "human" rather than
breaking.

**This datapack is now optional.** It exists only as a manual override — a non-zero
`racescale_race` score wins over the DAG detection, which is useful for testing a
shape without registering a race, or for using the mod in a world without DAG.

## Use

Works with **cheats off**: `/trigger` runs at permission level 0.

```
/trigger racescale_pick set 1    # human
/trigger racescale_pick set 2    # dwarf
/trigger racescale_pick set 3    # elf
/trigger racescale_pick set 4    # orc
```

With cheats on you can run `/function racescale:race/dwarf` instead, or
`/function racescale:reset` to go back to normal.

The scale re-applies automatically after death, because respawning rebuilds the
player entity and resets its attributes.

## Install

The datapack is per-world and cannot ship through `overrides/`, so copy it into a
world; the mod goes in the instance:

```
saves/<world>/datapacks/racescale/     <- this folder
mods/racescale-0.1.0.jar               <- built from ../racescale-mod
```

New datapacks are picked up when the world loads. `/reload` also works but needs
cheats, so with cheats off just exit to the title screen and re-enter.

## Notes

An elf at 1.2 stands 2.16 blocks and must sneak through standard 2-block doorways.
That is exactly what the Mythfolk elven doorway standard exists for — a top slab
above a normal door gives 2.5 blocks of clearance. See
[../docs/MYTHFOLK-PLAN.md](../docs/MYTHFOLK-PLAN.md). Orcs at 1.98 and dwarves at
1.44 clear ordinary doorways unaided.

Data pack format is `107`, taken from Terralith 26.2 — the authoritative 26.2 value.
