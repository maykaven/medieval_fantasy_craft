# The racescale MOD owns body shape now: it scales per axis (dwarf shorter,
# elf taller, orc wider) in the renderer and in getDimensions, which the uniform
# minecraft:scale attribute cannot do. This function therefore keeps the
# attribute NEUTRAL - applying both would compound (a dwarf would come out
# 0.8 x 0.8). The scoreboard set by race/*.mcfunction is what the mod reads.
#
# Without the mod installed this leaves the player unscaled; re-add the per-race
# values here if you ever want datapack-only uniform scaling back.
attribute @s minecraft:scale base set 1.0
