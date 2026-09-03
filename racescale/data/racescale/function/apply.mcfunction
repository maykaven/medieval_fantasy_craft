# Uniform scale via the vanilla attribute: armour, held items, hitbox and
# eye height all follow automatically, so equipment always fits.
execute if score @s racescale_race matches 1 run attribute @s minecraft:scale base set 1.0
execute if score @s racescale_race matches 2 run attribute @s minecraft:scale base set 0.8
execute if score @s racescale_race matches 3 run attribute @s minecraft:scale base set 1.2
# Orc: 10% bigger uniformly. True "20% wider" is non-uniform and the vanilla
# scale attribute is uniform only. See racescale/README.md.
execute if score @s racescale_race matches 4 run attribute @s minecraft:scale base set 1.1
execute unless score @s racescale_race matches 1..4 run attribute @s minecraft:scale base set 1.0
