# Dwarf -> scale 0.8 (20% shorter)
scoreboard players set @s racescale_race 2
function racescale:apply
tellraw @s {"text":"Heritage registered: Dwarf (body scale 0.8).","color":"gold"}
