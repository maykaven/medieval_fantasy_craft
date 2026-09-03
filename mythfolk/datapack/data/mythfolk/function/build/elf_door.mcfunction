# Elven doorway - the Mythfolk standard opening for elven buildings.
#
# Clearance is 2.5 blocks: two full blocks of doorway, plus the lower half of
# the third block left open by a TOP slab. An elf stands 2.16 blocks tall
# (scale 1.2), so this is the smallest opening an elf walks through without
# sneaking - a vanilla 2-block door is not enough.
#
# Built facing north, wall running east-west. Stand facing north.
#
#   y+2   log   [top slab]   log     <- 0.5 open beneath the slab
#   y+1   log   door upper   log
#   y     log   door lower   log

# jambs
setblock ~-1 ~ ~ minecraft:birch_log[axis=y]
setblock ~-1 ~1 ~ minecraft:birch_log[axis=y]
setblock ~-1 ~2 ~ minecraft:birch_log[axis=y]
setblock ~1 ~ ~ minecraft:birch_log[axis=y]
setblock ~1 ~1 ~ minecraft:birch_log[axis=y]
setblock ~1 ~2 ~ minecraft:birch_log[axis=y]

# door: lower first, then upper - the lower half only validates its partner on
# an update from above, which the upper placement itself provides
setblock ~ ~ ~ minecraft:birch_door[facing=north,half=lower,hinge=left,open=false,powered=false]
setblock ~ ~1 ~ minecraft:birch_door[facing=north,half=upper,hinge=left,open=false,powered=false]

# transom: a TOP slab occupies the upper half, leaving 0.5 open below it
setblock ~ ~2 ~ minecraft:birch_slab[type=top]

tellraw @s {"text":"Elven doorway placed - 2.5 blocks of clearance.","color":"green"}
