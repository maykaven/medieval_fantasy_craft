# Copy the /trigger value into the persistent race score, then apply
execute store result score @s racescale_race run scoreboard players get @s racescale_pick
scoreboard players reset @s racescale_pick
function racescale:apply
execute if score @s racescale_race matches 1 run tellraw @s {"text":"Heritage: Human - normal build.","color":"gold"}
execute if score @s racescale_race matches 2 run tellraw @s {"text":"Heritage: Dwarf - 20% shorter.","color":"gold"}
execute if score @s racescale_race matches 3 run tellraw @s {"text":"Heritage: Elf - 20% taller. Sneak through 2-block doorways.","color":"gold"}
execute if score @s racescale_race matches 4 run tellraw @s {"text":"Heritage: Orc - 10% bigger all round.","color":"gold"}
