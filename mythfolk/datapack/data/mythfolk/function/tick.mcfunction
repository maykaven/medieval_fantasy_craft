# A trigger disarms itself after each use, so re-enable every tick
scoreboard players enable @a mythfolk_build

# /trigger mythfolk_build set 1  -> place an elven doorway at your feet
execute as @a[scores={mythfolk_build=1..}] at @s run function mythfolk:build/elf_door
execute as @a[scores={mythfolk_build=1..}] run scoreboard players reset @s mythfolk_build
