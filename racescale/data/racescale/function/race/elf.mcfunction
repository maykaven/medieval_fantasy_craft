# Elf -> scale 1.2 (20% taller)
scoreboard players set @s racescale_race 3
function racescale:apply
tellraw @s {"text":"Heritage registered: Elf (body scale 1.2).","color":"gold"}
