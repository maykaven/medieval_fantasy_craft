# Keep /trigger usable for everyone (a trigger disarms itself after each use)
scoreboard players enable @a racescale_pick

# A player picked a race with /trigger racescale_pick set N
execute as @a[scores={racescale_pick=1..4}] run function racescale:from_trigger

# Respawning rebuilds the player entity and resets attributes, so re-apply
execute as @a[scores={racescale_deaths=1..}] run function racescale:respawn
